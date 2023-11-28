# VYTL Jiu Jitsu Website

## Requirements in Build
Website Pages (no user required)
- Home
- About
- Instructors
- Schedule
- Pricing
- FAQs
- Events (New(s) will generate as a feed)
- Sign Up
- Sign In

Authenticated user Pages
- Profile
  - Phone number (changable)
  - Email (changable)
  - Emergency Contact (changable)
  - Membership (only changable by admin, can submit request to be monthly or 90 day cancellation)
  - View Badges
  - Change password
  - Attendance
    - View all class attendance
    - View notes for that class  
- Communications (DM)
  - User to Admin
  - User to User

Admin area
- Dashboard
  - Finances
    - Income
    - Expenses
  - Student list
    - First Name
    - Last Name
    - Age
    - Belt
    - Membershbip
  - Classes (notes for upcoming classes this week)
  - Memberships (View all memberships and stats)
- Memberships
  - View memberships
  - Add new memberships
- Take payments
  - ACH recurring based on membership from profile
  - Credit card payments
- Attendance
  - Take attendance for each class
  - View all attendance (need filters)
- Create a new user (password: vytljj23)
  - Assign membership when created
- Students
  - View student list
  - Link parent and child accounts
  - Change membership (will change recurring draft)
  - Change user status (active | inactive)
- Finances
  - Income
    - Review income
      - Monthly
      - Quarterly
      - Yearly
  - Expenses
    - Enter new expenses (form)
    - Review expenses
      - Monthly
      - Quarterly
      - Yearly
  - Generate/Review P&L
    
  
## Models
- User
  - Profile (One to One with User)
  - Badges (One to One with User)
- Memberships (various membership options, each user will be assigned a membership to their profile)
- Class
  - Class Note
- Attend
- Member Income
- Expense
- New(s)


