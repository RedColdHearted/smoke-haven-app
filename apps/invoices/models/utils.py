from datetime import datetime, timedelta

def generate_two_week_pass_date():
    """Generate and return 2 week passed date for invoice."""
    return (datetime.now() + timedelta(weeks=2)).date