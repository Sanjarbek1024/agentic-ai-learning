from sqlalchemy import text
from database import SessionLocal



def execute_query(query):
    session = SessionLocal()
    
    try:
        result = session.execute(text(query))
        
        if query.strip().lower().startswith('select'):
            data = [dict(row) for row in result.mappings()]
            return data
            
        session.commit()
        return {"message": "Query executed successfully."}
    
    except Exception as e:
        session.rollback()
        return {'error': e}
    
    finally:
        session.close()
        
        
# result = execute_query("SELECT * FROM employees limit 10")
# print(result)

def get_all_employees():
    return execute_query("SELECT * FROM employees")

def get_employee_by_id(employee_id: int):
    query = f"SELECT * FROM employees WHERE id = {employee_id}"
    return execute_query(query)

def get_employees_by_department(department: str):
    query = f"""
        SELECT *
        FROM employees
        WHERE department = '{department}'
    """
    return execute_query(query)

def get_high_salary_employees(min_salary: int):
    query = f"""
        SELECT *
        FROM employees
        WHERE salary >= {min_salary}
    """
    return execute_query(query)

def get_employee_count():
    return execute_query(
        "SELECT COUNT(*) AS total_employees FROM employees"
    )
    
def get_average_salary():
    return execute_query(
        "SELECT AVG(salary) AS average_salary FROM employees"
    )
    
def get_top_paid_employees():
    query = """
        SELECT *
        FROM employees
        ORDER BY salary DESC
        LIMIT 5
    """
    return execute_query(query)

def get_department_statistics():
    query = """
        SELECT
            department,
            COUNT(*) AS employees,
            AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
    """
    return execute_query(query)