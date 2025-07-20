import json
from redis_client import redis_conn

QUEUE_NAME = "task_queue"


def enqueue_task(task_type, data):
    task = {"type": task_type, "data": data}
    redis_conn.lpush(QUEUE_NAME, json.dumps(task))
    print(f"Enqueued: {task}")


if __name__ == "__main__":
    enqueue_task("send_email", {"to": "user@example.com", "subject": "Welcome!"})
    enqueue_task("generate_pdf", {"doc_id": 42})
