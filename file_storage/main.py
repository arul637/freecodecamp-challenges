def number_of_files(file_size, file_unit, drive_size_gb):

    match file_unit:
        case "KB":
            return int((drive_size_gb*1000)/(file_size/1000))
        case "MB":
            return int((drive_size_gb*1000)/file_size)
        case "B":
            return int((drive_size_gb*1000)/(file_size/(1000*1000)))
        case _:
            return None 


print(number_of_files(500, "KB", 1))
print(number_of_files(50000, "B", 1))
print(number_of_files(5, "MB", 1))
print(number_of_files(4096, "B", 1.5))
print(number_of_files(220.5, "KB", 100))
print(number_of_files(4.5, "MB", 750))