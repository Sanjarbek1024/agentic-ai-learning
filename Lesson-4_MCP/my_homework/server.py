# from mcp.server.fastmcp import FastMCP
# # from tools.sql_tool import (
# #     execute_query,
# #     get_all_employees,
# #     get_employee_by_id,
# #     get_employees_by_department,
# #     get_high_salary_employees,
# #     get_employee_count,
# #     get_average_salary,
# #     get_department_statistics,
# #     get_top_paid_employees
# # )

# mcp = FastMCP("SQL MCP Server")

# # @mcp.tool()
# # def run_sql(query: str):
# #     """
# #     Execute any SQL query on the SQLite database.

# #     Args:
# #         query: Valid SQL query.

# #     Returns:
# #         Query result or execution status.
# #     """
# #     return execute_query(query)


# # @mcp.tool()
# # def all_employees():
# #     """
# #     Return all employees.
# #     """
# #     return get_all_employees()


# # @mcp.tool()
# # def employee_by_id(employee_id: int):
# #     """
# #     Get employee by ID.

# #     Args:
# #         employee_id: Employee ID.
# #     """
# #     return get_employee_by_id(employee_id)


# # @mcp.tool()
# # def employees_by_department(department: str):
# #     """
# #     Get employees from a specific department.

# #     Args:
# #         department: Department name.
# #     """
# #     return get_employees_by_department(department)


# # @mcp.tool()
# # def employees_with_high_salary(min_salary: int):
# #     """
# #     Get employees whose salary is greater than or equal to the given amount.

# #     Args:
# #         min_salary: Minimum salary.
# #     """
# #     return get_high_salary_employees(min_salary)


# # @mcp.tool()
# # def employee_count():
# #     """
# #     Return total number of employees.
# #     """
# #     return get_employee_count()


# # @mcp.tool()
# # def average_salary():
# #     """
# #     Return average salary of all employees.
# #     """
# #     return get_average_salary()


# # @mcp.tool()
# # def department_statistics():
# #     """
# #     Return statistics for each department.

# #     Returns:
# #         Employee count and average salary grouped by department.
# #     """
# #     return get_department_statistics()


# # @mcp.tool()
# # def top_paid_employees():
# #     """
# #     Return the top 5 highest-paid employees.

# #     Returns:
# #         A list of employees ordered by salary in descending order.
# #     """
# #     return get_top_paid_employees()


# if __name__ == "__main__":
#     mcp.run(transport='stdio')

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test Server")


@mcp.tool()
def hello() -> str:
    """Return a hello message."""
    return "Hello MCP"


if __name__ == "__main__":
    mcp.run(transport="stdio")