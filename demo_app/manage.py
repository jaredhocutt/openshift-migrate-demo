#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    # BEGIN: wait for database
    if sys.argv[1] == "migrate":
        import socket
        import time

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while sock.connect_ex(('postgresql', 5432)) != 0:
            print("Waiting on postgresql connection...")
            time.sleep(1)

        print("Connection to postgresql available")
    # END: wait for database

    execute_from_command_line(sys.argv)
