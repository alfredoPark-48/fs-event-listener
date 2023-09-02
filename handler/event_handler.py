import os
from watchdog.events import FileSystemEventHandler
from email_notifier.email_notifier import send_email_notification

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        file_name = os.path.basename(event.src_path)
        if event.is_directory:
            new_directory = event.src_path
            print(f"New directory created: {new_directory}")
            send_email_notification(f"New directory created: {new_directory}", "Directory created")
        else:
            if not (event.src_path.endswith("4913") or file_name.endswith('~') or file_name.startswith('.')):  # Skip the temporary file
                new_file = event.src_path
                print(f"New file created: {new_file}")
                send_email_notification(f"New file created: {new_file}", "File created")

    def on_deleted(self, event):
        file_name = os.path.basename(event.src_path)
        if event.is_directory:
            deleted_directory = event.src_path
            print(f"Directory deleted: {deleted_directory}")
            send_email_notification(f"Directory deleted: {deleted_directory}", "Directory removed")
        else:
            if not (event.src_path.endswith("4913") or file_name.endswith('~') or file_name.startswith('.')):  # Skip the temporary file
                deleted_file = event.src_path
                print(f"File deleted: {deleted_file}")
                send_email_notification(f"File deleted: {deleted_file}", "File removed")

    def on_modified(self, event):
        file_name = os.path.basename(event.src_path)
        if not (event.src_path.endswith("4913") or file_name.endswith('~') or file_name.startswith('.')):  # Skip the temporary file
            if not event.is_directory and os.path.getsize(event.src_path) != 0:
                print(f"File modified: {event.src_path}")
                send_email_notification(f"File modified: {event.src_path}", "File modified")

    def on_moved(self, event):
        src_file_name = os.path.basename(event.src_path)
        dest_file_name = os.path.basename(event.dest_path)

        # Check if only the file name has changed (not the content)
        if src_file_name == dest_file_name:
            if not (src_file_name.endswith("4913") or src_file_name.endswith('~') or src_file_name.startswith('.')):
                print(f"File modified: {event.src_path}")
                send_email_notification(f"File modified: {event.src_path}", "File modified")
        else:
            if event.is_directory:
                print(f"Directory moved/renamed from: {event.src_path} to {event.dest_path}")
                send_email_notification(f"Directory moved/renamed: {event.src_path} to {event.dest_path}", "Directory moved/renamed")
            else:
                if not (dest_file_name.endswith("4913") or dest_file_name.endswith('~') or dest_file_name.startswith('.')):
                    print(f"File moved/renamed from: {event.src_path} to {event.dest_path}")
                    send_email_notification(f"File moved/renamed: {event.src_path} to {event.dest_path}", "Directory moved/renamed")
