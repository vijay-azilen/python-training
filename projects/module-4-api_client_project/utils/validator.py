def validate_user(user):
    required_field = [
        "id",
        "name",
        "email"
    ]
    
    for field in required_field:
        if field not in user:
            raise ValueError(
                f"Missing field: {field}" 
            )
    return True