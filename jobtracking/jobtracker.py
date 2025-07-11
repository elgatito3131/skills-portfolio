import csv
import os

CSV_FILE = "jobs.csv"
HEADERS = ["company", "position", "date_applied", "status", "notes"]

class Job:
    def __init__(self, company, position, date_applied, status, notes):
        self.company = company
        self.position = position
        self.date_applied = date_applied
        self.status = status
        self.notes = notes

    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "date_applied": self.date_applied,
            "status": self.status,
            "notes": self.notes,
        }

    def __str__(self):
        return (
            f"Company: {self.company}\n"
            f"Position: {self.position}\n"
            f"Date: {self.date_applied}\n"
            f"Status: {self.status}\n"
            f"Notes: {self.notes}"
        )

def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()

def save_job(job):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writerow(job.to_dict())

def read_jobs():
    jobs = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                job = Job(
                    row["company"],
                    row["position"],
                    row["date_applied"],
                    row["status"],
                    row["notes"]
                )
                jobs.append(job)
    return jobs


def write_all_jobs(jobs):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job.to_dict())
            
            
def write_all_jobs(jobs):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writeheader()
        for job in jobs:
            writer.writerow(job.to_dict())

def add_job():
    print("Enter job info:")
    company = input("Company: ")
    position = input("Position: ")
    date = input("Date applied (YYYY-MM-DD): ")
    status = input("Status (applied/interviewed/offer/rejected): ")
    notes = input("Notes: ")
    job = Job(company, position, date, status, notes)
    save_job(job)
    print("✅ Job saved.")

def search_jobs():
    jobs = read_jobs()
    if not jobs:
        print("No jobs available to search.")
        return

    print("\nSearch by:")
    print("1. Company")
    print("2. Status")
    choice = input("Choose an option: ")

    if choice == "1":
        keyword = input("Enter company name (partial ok): ").lower()
        filtered = [job for job in jobs if keyword in job.company.lower()]
    elif choice == "2":
        keyword = input("Enter status (e.g. applied/interviewed): ").lower()
        filtered = [job for job in jobs if keyword == job.status.lower()]
    else:
        print("Invalid search option.")
        return

    if filtered:
        for idx, job in enumerate(filtered, 1):
            print(f"\nMatch #{idx}")
            print(job)
    else:
        print("No matching jobs found.")

def view_jobs():
    jobs = read_jobs()
    if not jobs:
        print("No jobs found.")
    else:
        for idx, job in enumerate(jobs, 1):
            print(f"\nJob #{idx}")
            print(job)

def edit_job():
    jobs = read_jobs()
    if not jobs:
        print("No jobs to edit.")
        return

    view_jobs()
    try:
        idx = int(input("Enter job number to edit: ")) - 1
        if idx < 0 or idx >= len(jobs):
            print("Invalid number.")
            return
        job = jobs[idx]
        print("Leave blank to keep current value.")

        company = input(f"Company ({job.company}): ") or job.company
        position = input(f"Position ({job.position}): ") or job.position
        date = input(f"Date applied ({job.date_applied}): ") or job.date_applied
        status = input(f"Status ({job.status}): ") or job.status
        notes = input(f"Notes ({job.notes}): ") or job.notes

        jobs[idx] = Job(company, position, date, status, notes)
        write_all_jobs(jobs)
        print("✅ Job updated.")

    except ValueError:
        print("Invalid input.")

def delete_job():
    jobs = read_jobs()
    if not jobs:
        print("No jobs to delete.")
        return

    view_jobs()
    try:
        idx = int(input("Enter job number to delete: ")) - 1
        if idx < 0 or idx >= len(jobs):
            print("Invalid number.")
            return

        confirm = input(f"Are you sure you want to delete job #{idx + 1}? (y/n): ").lower()
        if confirm == "y":
            jobs.pop(idx)
            write_all_jobs(jobs)
            print("🗑️ Job deleted.")
        else:
            print("Cancelled.")

    except ValueError:
        print("Invalid input.")

def menu():
    init_csv()
    while True:
        print("\n=== Job Tracker (CSV) ===")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Edit Job")
        print("4. Delete Job")
        print("5. Search Jobs")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            edit_job()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            search_jobs()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
