def print_queue_simulation():
    queue = LinkedQueue()

    print("\n===== PRINT QUEUE SIMULATION =====")

    number = int(input("How many print jobs? "))

    for i in range(number):
        print("\nJob", i + 1)

        job_id = input("Enter Job ID: ")
        pages = int(input("Enter number of pages: "))

        job = {
            "id": job_id,
            "pages": pages
        }

        queue.enqueue(job)

    print("\n===== WAITING PRINT JOBS =====")

    for job in queue.display():
        print("Job ID:", job["id"],
              "| Pages:", job["pages"])

    print("\n===== PRINTING JOBS =====")

    order = 1

    while not queue.is_empty():
        job = queue.dequeue()

        print("Print Order:", order)
        print("Job ID:", job["id"])
        print("Pages:", job["pages"])
        print("Status: Printed")
        print("-----------------------")

        order += 1

    print("All print jobs completed!")