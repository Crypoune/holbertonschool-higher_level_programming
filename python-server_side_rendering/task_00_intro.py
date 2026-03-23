#!/usr/bin/python3
"""Creating a Simple Templating Program module"""
import os
import logging

logging.basicConfig(level=logging.ERROR)

def generate_invitations(template, attendees):
    """Function that generates personalized invitations from a template with placeholders and a list of objects"""
    if not isinstance(template, str):
        logging.error("Invalid input: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid input: attendees is not a list of dictionaries.")
        return
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        personalized_invitation = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = f"output_{index}.txt"

        if os.path.exists(output_filename):
            logging.error(f"File {output_filename} already exists. Skipping file creation.")
            continue

        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(personalized_invitation)
            print(f"Generated invitation: {output_filename}")
        except Exception as e:
            logging.error(f"Error writing file {output_filename}: {e}")
