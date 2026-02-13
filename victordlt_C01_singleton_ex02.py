from datetime import datetime

class EventLogger:
    _instance = None
    _event_logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventLogger, cls).__new__(cls)
        return cls._instance


    def log_event(self, event_message): 
        timnestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") 
        self._event_logs.append(f"{timnestamp} : {event_message}")

    def display_logs(self):
        for log in self._event_logs:
            print(log)



logger = EventLogger()
logger.log_event("User logged in")
logger.log_event("User performed an action")
logger2 = EventLogger()
logger2.log_event("User logged out")
logger3 = EventLogger()
logger3.log_event("User logged in again")
logger3.log_event("User performed another action")

logger.display_logs()
