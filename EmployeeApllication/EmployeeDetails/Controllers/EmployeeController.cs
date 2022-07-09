using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using EmployeeDetails.DbContext;

namespace EmployeeDetails.Controllers
{
    public class EmployeeController : Controller
    {
        EmployeesDbEntities dbEmployee = new EmployeesDbEntities();
        // GET: Emplyee        

        public ActionResult Employee(Employee obj)
        {
            if (obj != null) return View(obj);
            return View();
        }

        [HttpPost]
        public ActionResult AddEmployee(Employee model)
        {
            Employee tblEmpoyee = new Employee();
            if (ModelState.IsValid)
            {
                tblEmpoyee.EmployeeId = model.EmployeeId;
                tblEmpoyee.FirstName = model.FirstName;
                tblEmpoyee.LastName = model.LastName;
                tblEmpoyee.EmailId = model.EmailId;
                tblEmpoyee.MobileNo = model.MobileNo;
                tblEmpoyee.City = model.City;
                tblEmpoyee.Country = model.Country;
                if (model.EmployeeId == 0)
                {
                    dbEmployee.Employees.Add(tblEmpoyee);
                    dbEmployee.SaveChanges();
                }
                else
                {
                    dbEmployee.Entry(tblEmpoyee).State = EntityState.Modified;
                    dbEmployee.SaveChanges();
                }
            }

            ModelState.Clear();
            return View("Employee");
        }

        public ActionResult EmployeeList()
        {
            var empList = dbEmployee.Employees.ToList();
            return View(empList);
        }

        public ActionResult DeleteEmployee(int id)
        {
            var empToRemove = dbEmployee.Employees.Where(x => x.EmployeeId == id).First();
            dbEmployee.Employees.Remove(empToRemove);
            dbEmployee.SaveChanges();

            var empList = dbEmployee.Employees.ToList();

            return View("EmployeeList", empList);
        }

    }
}