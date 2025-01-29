import logging
import uuid

logging.basicConfig(filename='Logs/activity.log', level=logging.INFO)

def generate_task_id():
    return str(uuid.uuid4())

def log_event(task_id, event):
    logging.info(f"Task ID: {task_id} - {event}")

def log_error(task_id, error):
    logging.error(f"Task ID: {task_id} - {error}")