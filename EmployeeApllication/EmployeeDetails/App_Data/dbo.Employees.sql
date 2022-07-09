CREATE TABLE [dbo].[Employees] (
    [EmployeeId] INT          IDENTITY (1, 1) NOT NULL,
    [FirstName]  VARCHAR (25) NOT NULL,
    [LastName]   VARCHAR (25) NOT NULL,
    [MobileNo]   VARCHAR (15) NULL,
    [EmailId]    VARCHAR (50) NULL,
    [City]       VARCHAR (20) NULL,
    [Country]    VARCHAR (20) NULL,
    PRIMARY KEY CLUSTERED ([EmployeeId] ASC)
);

