# encoding: utf-8
from celery.utils.log import get_task_logger
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
log = get_task_logger(__name__)
import requests

@shared_task(bind=True, default_retry_delay=60)
def webhook_task(self, task, url, result, headers=None, **kwargs):
    log.debug("TODO: kwargs: %s", kwargs)
    max_retries=int(kwargs.get("max_retries", 0))
    countdown=int(kwargs.get("countdown", 60))
    timeout=int(kwargs.get("timeout", 10)) # TODO: 考虑使用 CELERY_WEBHOOK_DEFAULT_TIMEOUT
    prepared = requests.Request("GET", url, json={
        "result": result,
        "task": task,
        },
        headers=headers,
    ).prepare()
    log.debug("req: %s\nheaders:%s", prepared.body, prepared.headers)
    res = None
    need_retry = False
    try:
        res = requests.session().send(prepared, timeout=timeout, verify=False, allow_redirects=0)
    except Exception as e:
        log.exception(e)
    finally:
        if not res or res.status_code > 299 or res.status_code < 200:
            need_retry = True

    log.error("need_retry %s %d", need_retry, max_retries)
    if need_retry and max_retries>0:
        log.error("retries .....")
        try:
            self.retry(max_retries=max_retries, countdown=countdown)
        except MaxRetriesExceededError as e:
            log.error("max_retries exceeded %s", e)

def webhook(req, url, result, headers=None, **kwargs):
    log.debug("TODO: kwargs: %s", kwargs)
    return webhook_task.apply_async((
        {"task_id": req.id},
        url,
        result,
        headers,
        ),
        kwargs,
    );

