def https_status(status):
    match status:
        case 200:
            return "OK"
        case 500:
            return "Internal Server Error"
        case 404:
            return "Not Found"
        case _: # This is a default case 
            return "Unknown Status"
        
print(https_status(200))
print(https_status(404))
print(https_status(500))
print(https_status(685))