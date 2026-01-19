import json

def validate_wbc(request_json):
    # 1. Validation for missing fields
    if not request_json or 'wbc' not in request_json:
        return {"error": "The 'wbc' field is required."}, 400
    
    # 2. Validation for non-numeric data
    try:
        wbc_value = float(request_json['wbc'])
    except (ValueError, TypeError):
        return {"error": "'wbc' must be a number."}, 400

    # 3. WBC Range Logic
    if 4.0 <= wbc_value <= 11.0:
        status = "normal"
        category = "Normal (4-11)"
    else:
        status = "abnormal"
        category = "Outside Range (4-11)"

    # 4. Response Contract
    return {
        "wbc": wbc_value,
        "status": status,
        "category": category
    }, 200

