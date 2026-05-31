# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên (dùng đúng key)
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên (dùng đúng key)
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên (dùng đúng key)
employee["status"] = "official"

# Thêm lương cơ bản (dùng gán key mới, không dùng append)
employee["base_salary"] = 15000000

# Xóa phòng ban (dùng đúng key)
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)