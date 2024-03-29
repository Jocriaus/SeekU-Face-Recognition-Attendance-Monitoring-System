USE [seeku_database]
GO
/****** Object:  Table [dbo].[tbl_personnel]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_personnel](
	[personnel_no] [nvarchar](50) NOT NULL,
	[personnel_firstname] [varchar](50) NULL,
	[personnel_lastname] [varchar](50) NULL,
	[personnel_middlename] [varchar](50) NULL,
	[personnel_contact_no] [nvarchar](50) NULL,
	[personnel_address] [varchar](50) NULL,
	[personnel_type] [varchar](50) NULL,
	[personnel_status] [varchar](50) NULL,
 CONSTRAINT [PK_tbl_personnel] PRIMARY KEY CLUSTERED 
(
	[personnel_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_personnel_attendance]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_personnel_attendance](
	[personnel_attendance_no] [int] IDENTITY(1,1) NOT NULL,
	[personnel_no] [nvarchar](50) NULL,
	[personnel_attendance_date] [date] NULL,
	[personnel_time_in] [time](7) NULL,
	[personnel_time_out] [time](7) NULL,
 CONSTRAINT [PK_tbl_personnel_attendance] PRIMARY KEY CLUSTERED 
(
	[personnel_attendance_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_setting]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_setting](
	[setting_no] [int] IDENTITY(1,1) NOT NULL,
	[password_length] [int] NULL,
	[login_attempt] [int] NULL,
	[student_setting] [datetime] NULL,
 CONSTRAINT [PK_tbl_setting] PRIMARY KEY CLUSTERED 
(
	[setting_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_student]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_student](
	[student_no] [int] NOT NULL,
	[student_firstname] [varchar](50) NULL,
	[student_lastname] [varchar](50) NULL,
	[student_middlename] [varchar](50) NULL,
	[student_program] [varchar](50) NULL,
	[student_section] [varchar](50) NULL,
	[student_contact_no] [nvarchar](50) NULL,
	[student_address] [varchar](max) NULL,
	[student_status] [varchar](50) NOT NULL,
 CONSTRAINT [PK_tbl_student] PRIMARY KEY CLUSTERED 
(
	[student_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_student_attendance]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_student_attendance](
	[student_attendance_no] [int] IDENTITY(1,1) NOT NULL,
	[student_no] [int] NULL,
	[student_attendance_date] [date] NULL,
	[student_time_in] [time](7) NULL,
	[student_time_out] [time](7) NULL,
 CONSTRAINT [PK_tbl_student_attendance] PRIMARY KEY CLUSTERED 
(
	[student_attendance_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_user]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_user](
	[user_no] [int] IDENTITY(1,1) NOT NULL,
	[username] [varchar](50) NULL,
	[password] [varchar](50) NULL,
	[user_firstname] [varchar](50) NULL,
	[user_lastname] [varchar](50) NULL,
	[user_type] [varchar](50) NULL,
	[user_status] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_visitor]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_visitor](
	[visitor_no] [int] IDENTITY(1,1) NOT NULL,
	[visitor_firstname] [varchar](50) NULL,
	[visitor_lastname] [varchar](50) NULL,
	[visitor_contact_no] [int] NULL,
	[visitor_address] [varchar](50) NULL,
	[visitor_status] [varchar](50) NULL,
 CONSTRAINT [PK_tbl_visitor] PRIMARY KEY CLUSTERED 
(
	[visitor_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tbl_visitor_attendance]    Script Date: 16/03/2023 12:54:56 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tbl_visitor_attendance](
	[visitor_attendance_no] [int] IDENTITY(1,1) NOT NULL,
	[visitor_no] [int] NULL,
	[visitor_attendance_date] [date] NULL,
	[visitor_time_in] [time](7) NULL,
	[visitor_time_out] [time](7) NULL,
 CONSTRAINT [PK_tbl_visitor_attendance] PRIMARY KEY CLUSTERED 
(
	[visitor_attendance_no] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[tbl_personnel] ADD  CONSTRAINT [DF_tbl_personnel_personnel_status]  DEFAULT ('IsActive') FOR [personnel_status]
GO
ALTER TABLE [dbo].[tbl_student] ADD  CONSTRAINT [DF_tbl_student_student_status]  DEFAULT ('IsActive') FOR [student_status]
GO
ALTER TABLE [dbo].[tbl_user] ADD  CONSTRAINT [DF_tbl_user_user_status]  DEFAULT ('IsActive') FOR [user_status]
GO
ALTER TABLE [dbo].[tbl_visitor] ADD  CONSTRAINT [DF_tbl_visitor_visitor_status]  DEFAULT ('IsActive') FOR [visitor_status]
GO
ALTER TABLE [dbo].[tbl_personnel_attendance]  WITH CHECK ADD  CONSTRAINT [FK_tbl_personnel_attendance_tbl_personnel] FOREIGN KEY([personnel_no])
REFERENCES [dbo].[tbl_personnel] ([personnel_no])
GO
ALTER TABLE [dbo].[tbl_personnel_attendance] CHECK CONSTRAINT [FK_tbl_personnel_attendance_tbl_personnel]
GO
ALTER TABLE [dbo].[tbl_student_attendance]  WITH CHECK ADD  CONSTRAINT [FK_tbl_student_attendance_tbl_student] FOREIGN KEY([student_no])
REFERENCES [dbo].[tbl_student] ([student_no])
GO
ALTER TABLE [dbo].[tbl_student_attendance] CHECK CONSTRAINT [FK_tbl_student_attendance_tbl_student]
GO
ALTER TABLE [dbo].[tbl_visitor_attendance]  WITH CHECK ADD  CONSTRAINT [FK_tbl_visitor_attendance_tbl_visitor] FOREIGN KEY([visitor_no])
REFERENCES [dbo].[tbl_visitor] ([visitor_no])
GO
ALTER TABLE [dbo].[tbl_visitor_attendance] CHECK CONSTRAINT [FK_tbl_visitor_attendance_tbl_visitor]
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Possible Values: IsActive, IsArchive, IsDeleted' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'tbl_personnel', @level2type=N'COLUMN',@level2name=N'personnel_status'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Possible Variables: IsActive, IsArchive, IsDeleted' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'tbl_student', @level2type=N'COLUMN',@level2name=N'student_status'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'tbl_student'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Possible Values: IsActive, IsArchive, IsDeleted' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'tbl_user', @level2type=N'COLUMN',@level2name=N'user_status'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'Possible Values: IsActive, IsArchive, IsDeleted' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'tbl_visitor', @level2type=N'COLUMN',@level2name=N'visitor_status'
GO
