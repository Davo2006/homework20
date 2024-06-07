import datetime

class HospitalAccount():
    def __init__(self) -> None:
        self.schedule = None
    def create_schedule(self):
        dt = datetime.datetime.now()+datetime.timedelta(days=1)
        self.schedule = dt
        print(f'Scheduled for {dt.strftime("%d/%m/%Y %I:%M %p")}')
    def remove_schedule(self):
        if not self.schedule:
            print("No schedule found")
            return
        self.schedule = None
        print("Schedule removed successfully")
account = HospitalAccount()
account.create_schedule()
account.remove_schedule()