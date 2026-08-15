import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process Each Attendee and Generate Output Files
    for index, attendee in enumerate(attendees, start=1):
        # Extract values or default to "N/A" if missing or None
        name = attendee.get("name")
        name = name if name is not None else "N/A"

        event_title = attendee.get("event_title")
        event_title = event_title if event_title is not None else "N/A"

        event_date = attendee.get("event_date")
        event_date = event_date if event_date is not None else "N/A"

        event_location = attendee.get("event_location")
        event_location = event_location if event_location is not None else "N/A"

        # Replace placeholders in the template
        personalized_content = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = f"output_{index}.txt"

        # Write to output file
        try:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(personalized_content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")

    print(f"Successfully generated {len(attendees)} invitation file(s).")
