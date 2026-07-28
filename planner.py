def create_plan(user_request):
    """
    Creates a dynamic execution plan based on the user's request.
    """

    request = user_request.lower()

    if "proposal" in request:
        tasks = [
            "Understand the project proposal request",
            "Identify proposal sections",
            "Generate proposal content using Gemini AI",
            "Create Microsoft Word proposal",
            "Return the generated proposal"
        ]

    elif "meeting" in request:
        tasks = [
            "Understand the meeting request",
            "Identify meeting participants",
            "Generate meeting minutes",
            "Create Microsoft Word document",
            "Return the generated meeting minutes"
        ]

    elif "report" in request:
        tasks = [
            "Understand the report request",
            "Identify report structure",
            "Generate report content",
            "Create Microsoft Word report",
            "Return the report"
        ]

    else:
        tasks = [
            "Understand the user request",
            "Determine the document type",
            "Generate document using Gemini AI",
            "Create Microsoft Word document",
            "Return the generated document"
        ]

    return tasks