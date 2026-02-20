# CHANDRABHUSHAN ONLINE - Complete Project Documentation

## 📋 Project Overview (प्रोजेक्ट अवलोकन)

**CHANDRABHUSHAN ONLINE** एक Django-based Online Service Center Website है जो Government Forms, Job Applications, Admit Cards, Results, और Scholarships के लिए services provide करता है।

---

## 🚀 Project Setup (प्रोजेक्ट सेटअप)

### Step 1: Virtual Environment बनाएं
```bash
python -m venv venv
venv\Scripts\activate    # Windows के लिए
# या
source venv/bin/activate  # Mac/Linux के लिए
```

### Step 2: Dependencies Install करें
```bash
pip install -r requirements.txt
```

**Required Packages:**
- Django >= 4.2, < 5.0
- Pillow >= 10.0.0 (images के लिए)

### Step 3: Database Migrations Run करें
```bash
python manage.py makemigrations
python manage.py migrate
```

यह database tables बनाएगा:
- `shop_product` - Products के लिए
- `shop_service` - Services/Updates के लिए
- `shop_inquiry` - Customer inquiries के लिए
- Django के default tables (auth, admin, etc.)

### Step 4: Admin User बनाएं
```bash
python manage.py createsuperuser
```
Username, email (optional), और password enter करें।

### Step 5: Server Start करें
```bash
python manage.py runserver
```

### Step 6: Website Access करें
- **Website:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin-panel/login/
- **Django Admin:** http://127.0.0.1:8000/admin-django/

---

## 📁 Project Structure (प्रोजेक्ट संरचना)

```
CHANDRABHUSHAN ONLINE/
│
├── manage.py                          # Django project का main entry point
├── requirements.txt                   # Python packages list
├── db.sqlite3                        # SQLite database (auto-created)
├── .gitignore                        # Git ignore file
│
├── chandrabhushan_online/            # Main project folder
│   ├── __init__.py
│   ├── settings.py                   # Project settings (DATABASE, INSTALLED_APPS, etc.)
│   ├── urls.py                      # Root URL configuration
│   ├── wsgi.py                      # WSGI configuration (production)
│   └── asgi.py                      # ASGI configuration
│
├── shop/                             # Main application
│   ├── __init__.py
│   ├── models.py                    # Database models (Product, Service, Inquiry)
│   ├── views.py                     # All views (public + admin)
│   ├── urls.py                      # App URLs
│   ├── forms.py                     # Forms (InquiryForm, ProductForm, ServiceForm)
│   ├── admin.py                     # Django admin configuration
│   │
│   ├── migrations/                  # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_service.py
│   │   └── 0003_inquiry_updates.py
│   │
│   ├── templates/shop/              # HTML templates
│   │   ├── base.html               # Base template (navbar, footer)
│   │   ├── home.html               # Home page
│   │   ├── about.html              # About page
│   │   ├── products.html            # Products listing
│   │   ├── product_detail.html      # Single product view
│   │   ├── services.html            # Services listing
│   │   ├── service_detail.html      # Single service view
│   │   ├── service_inquiry.html     # Service inquiry form
│   │   ├── gallery.html             # Gallery page
│   │   ├── contact.html             # Contact page
│   │   │
│   │   └── admin/                   # Admin templates
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── inquiry_list.html
│   │       ├── product_list.html
│   │       ├── product_form.html
│   │       ├── product_confirm_delete.html
│   │       ├── service_list.html
│   │       ├── service_form.html
│   │       └── service_confirm_delete.html
│   │
│   └── static/shop/                 # Static files
│       └── css/
│           └── style.css           # Custom CSS (responsive design)
│
└── media/                           # Uploaded files (auto-created)
    ├── products/                    # Product images
    └── services/                    # Service images/banners
```

---

## 🗄️ Database Models (डेटाबेस मॉडल)

### 1. Product Model
```python
- name: CharField (Product का नाम)
- description: TextField (विवरण)
- price: DecimalField (कीमत)
- image: ImageField (तस्वीर)
- created_date: DateTimeField (बनाने की तारीख)
```

### 2. Service Model
```python
- title: CharField (Service का शीर्षक)
- category: CharField (Job/Admit Card/Form/Result/Scholarship)
- short_description: TextField (छोटा विवरण - 300 chars)
- full_description: TextField (पूरा विवरण)
- required_documents: TextField (आवश्यक दस्तावेज)
- eligibility: TextField (योग्यता - optional)
- start_date: DateField (शुरुआत की तारीख)
- end_date: DateField (अंतिम तारीख)
- apply_link: URLField (Official apply link)
- image: ImageField (Banner image)
- created_at: DateTimeField (बनाने की तारीख)

Methods:
- is_active() - Check करता है service active है या नहीं
- is_expired() - Check करता है service expired है या नहीं
```

### 3. Inquiry Model
```python
- name: CharField (ग्राहक का नाम)
- phone: CharField (फोन नंबर)
- email: EmailField (ईमेल)
- message: TextField (संदेश)
- related_service: ForeignKey (कौन सी service के लिए inquiry)
- created_at: DateTimeField (तारीख)
- read: BooleanField (पढ़ा गया या नहीं)
```

---

## 🌐 Website Pages (वेबसाइट पेज)

### Public Pages (सार्वजनिक पेज)

#### 1. Home Page (`/`)
- Website introduction
- Latest services highlights (6 services)
- Quick links
- Service categories overview

#### 2. About Us (`/about/`)
- Shop history
- Owner information
- Trust and quality information
- Why choose us section

#### 3. Products (`/products/`)
- All products listing
- Product cards with image, name, price
- View details button

#### 4. Services & Latest Updates (`/services/`)
- **Features:**
  - Category filtering (Job, Admit Card, Form, Result, Scholarship)
  - Active/Expired/Upcoming status badges
  - Service cards with dates
  - View details button
- **Status Logic:**
  - **Active** (Green): Current date between start_date and end_date
  - **Expired** (Gray): Current date > end_date
  - **Upcoming** (Yellow): Current date < start_date

#### 5. Service Detail (`/services/<id>/`)
- Full service description
- Required documents list
- Eligibility criteria
- Important dates (start & end)
- Official apply link button
- **"Contact to Fill Form"** button (opens inquiry form)

#### 6. Service Inquiry (`/services/<id>/inquiry/`)
- Inquiry form for specific service
- Fields: Name, Phone, Email, Message
- Automatically links inquiry to service
- Success message after submission

#### 7. Gallery (`/gallery/`)
- Product images gallery
- Click to view product details

#### 8. Contact (`/contact/`)
- Phone: 7488578184
- Email: infochandrabhushan74@gmail.com
- WhatsApp button
- Google Map location
- General inquiry form

---

## 🔐 Admin Panel (एडमिन पैनल)

### Admin Login (`/admin-panel/login/`)
- Secure login with Django authentication
- Uses superuser credentials

### Admin Dashboard (`/admin-panel/`)
**Statistics Cards:**
- Total Products count
- Total Services count
- Total Inquiries count
- Unread Inquiries count

**Quick Actions:**
- Add Product button
- Add Service/Update button

**Recent Inquiries Table:**
- Customer name, phone, email
- Related service name
- Message preview
- Date and read status
- View all link

### Product Management (`/admin-panel/products/`)
- **List Products:** View all products with image, name, price
- **Add Product:** Form with name, description, price, image
- **Edit Product:** Update product details and image
- **Delete Product:** Confirmation before deletion

### Service Management (`/admin-panel/services/`)
- **List Services:** View all services with status badges
- **Add Service:** Complete form with:
  - Title, category, descriptions
  - Start date, end date
  - Required documents, eligibility
  - Apply link, image/banner
- **Edit Service:** Update all service details
- **Delete Service:** Confirmation before deletion

### Inquiry Management (`/admin-panel/inquiries/`)
- **View All Inquiries:** Complete list with:
  - Customer name, phone, email
  - Related service (which service they inquired about)
  - Full message
  - Date and read status
- **Mark as Read:** Mark inquiries as read/unread
- **Filter:** See which service each inquiry is related to

---

## 🔄 How It Works (कैसे काम करता है)

### User Flow (यूजर फ्लो)

1. **User visits website** → Home page
2. **Views services** → `/services/` page
3. **Clicks on a service** → Service detail page
4. **Clicks "Contact to Fill Form"** → Inquiry form opens
5. **Fills form** → Name, Phone, Email, Message
6. **Submits** → Inquiry saved with service reference
7. **Admin receives notification** → Sees inquiry in dashboard

### Admin Flow (एडमिन फ्लो)

1. **Admin logs in** → `/admin-panel/login/`
2. **Views dashboard** → Sees statistics and recent inquiries
3. **Adds new service** → Fills service form with all details
4. **Service appears** → On public `/services/` page
5. **Views inquiries** → Sees which service customer needs help with
6. **Contacts customer** → Uses phone/email from inquiry

### Service Status Logic (सर्विस स्टेटस लॉजिक)

```python
# Service model में methods:

def is_active(self):
    today = timezone.now().date()
    return self.start_date <= today <= self.end_date

def is_expired(self):
    today = timezone.now().date()
    return today > self.end_date

# Template में use:
{% if service.is_active %}
    <span class="badge bg-success">Active</span>
{% elif service.is_expired %}
    <span class="badge bg-secondary">Expired</span>
{% else %}
    <span class="badge bg-warning">Upcoming</span>
{% endif %}
```

---

## 📱 Responsive Design (रिस्पॉन्सिव डिज़ाइन)

Website सभी devices पर perfectly काम करता है:

- **Mobile Phones** (320px - 575px)
  - Stacked layout
  - Smaller fonts
  - Touch-friendly buttons
  - Responsive tables

- **Tablets** (576px - 991px)
  - Flexible grid
  - Balanced layout

- **Desktop** (992px+)
  - Full layout
  - All features visible

**Features:**
- Bootstrap 5 responsive grid
- Mobile-first CSS
- Touch-friendly buttons (min 44px)
- Responsive images (`img-fluid`)
- Horizontal scroll for tables on mobile
- Collapsible navbar on mobile

---

## 🎨 UI Features (यूआई फीचर्स)

1. **Modern Bootstrap 5 Design**
2. **Floating WhatsApp Button** (bottom-right corner)
3. **Professional Navbar** (fixed top, responsive)
4. **Footer** with quick links and contact info
5. **Status Badges** (Active/Expired/Upcoming)
6. **Category Filtering** (for services)
7. **Card Layout** for products and services
8. **Breadcrumb Navigation**
9. **Alert Messages** (success/error notifications)
10. **Responsive Forms**

---

## ⚙️ Configuration (कॉन्फ़िगरेशन)

### Contact Information Update करें:

1. **Phone Number:**
   - File: `shop/templates/shop/base.html` (line 75)
   - File: `shop/templates/shop/contact.html` (line 15)
   - Current: `7488578184`

2. **Email:**
   - File: `shop/templates/shop/base.html` (line 76)
   - File: `shop/templates/shop/contact.html` (line 18)
   - Current: `infochandrabhushan74@gmail.com`

3. **WhatsApp:**
   - File: `shop/templates/shop/base.html` (line 85)
   - File: `shop/templates/shop/contact.html` (line 21)
   - Current: `917488578184` (format: country code + number, no spaces)

4. **Google Map:**
   - File: `shop/templates/shop/contact.html` (line 55)
   - Replace iframe `src` with your Google Map embed URL

### Settings Configuration:

**File:** `chandrabhushan_online/settings.py`

- `DEBUG = True` (development के लिए)
- `ALLOWED_HOSTS = ['*']` (production में specific domain add करें)
- `MEDIA_URL = 'media/'` (uploaded files का URL)
- `MEDIA_ROOT = BASE_DIR / 'media'` (uploaded files का folder)
- `STATIC_URL = 'static/'` (CSS/JS files का URL)

---

## 🔧 Technical Details (तकनीकी विवरण)

### URL Routing:
- **Root URLs:** `chandrabhushan_online/urls.py`
- **App URLs:** `shop/urls.py`
- **URL Namespace:** `shop` (use: `{% url 'shop:home' %}`)

### Views:
- **Public Views:** `shop/views.py` में functions
- **Admin Views:** `@login_required` decorator के साथ
- **Service Inquiry:** Automatically links to service

### Forms:
- **InquiryForm:** Name, Phone, Email, Message, Related Service
- **ProductForm:** Name, Description, Price, Image
- **ServiceForm:** All service fields

### Static Files:
- **CSS:** `shop/static/shop/css/style.css`
- **Bootstrap:** CDN से load होता है
- **Icons:** Bootstrap Icons (CDN)

### Media Files:
- **Upload Location:** `media/products/` और `media/services/`
- **Served in Development:** Automatically via Django
- **Production:** Web server configuration needed

---

## 📝 Common Tasks (सामान्य कार्य)

### नया Service Add करना:
1. Admin panel login करें
2. "Add Service/Update" button click करें
3. Form fill करें:
   - Title, Category select करें
   - Start Date और End Date set करें
   - Documents list add करें
   - Image upload करें (optional)
   - Apply link add करें (optional)
4. Save करें
5. Service automatically public page पर दिखेगा

### Customer Inquiry देखना:
1. Admin dashboard पर जाएं
2. "View All" inquiries पर click करें
3. देखें:
   - Customer का नाम, phone, email
   - कौन सी service के लिए inquiry है
   - Message
   - Date और read status
4. Customer को contact करें

### Service Status Check करना:
- Service automatically status show करता है:
  - **Active:** अगर आज की date start और end date के बीच है
  - **Expired:** अगर end date गुजर गई है
  - **Upcoming:** अगर start date अभी नहीं आई है

---

## 🐛 Troubleshooting (समस्या निवारण)

### Database Error:
```bash
# अगर "no such table" error आए:
python manage.py makemigrations
python manage.py migrate
```

### Static Files नहीं दिख रहे:
```bash
# Collect static files:
python manage.py collectstatic
```

### Images Upload नहीं हो रहे:
- `media/` folder check करें (auto-create होना चाहिए)
- File permissions check करें
- `settings.py` में `MEDIA_ROOT` और `MEDIA_URL` check करें

### Admin Login नहीं हो रहा:
```bash
# नया superuser बनाएं:
python manage.py createsuperuser
```

---

## 📞 Support & Contact (सहायता और संपर्क)

- **Phone:** 7488578184
- **Email:** infochandrabhushan74@gmail.com
- **WhatsApp:** [Click to Chat](https://wa.me/917488578184)

---

## 📄 License & Credits (लाइसेंस और क्रेडिट)

- **Framework:** Django 4.2
- **Frontend:** Bootstrap 5
- **Icons:** Bootstrap Icons
- **Database:** SQLite (development)

---

## 🎯 Future Enhancements (भविष्य में सुधार)

Possible features to add:
- Email notifications for new inquiries
- Service search functionality
- PDF download for service details
- Customer account system
- Payment integration
- SMS notifications
- Multi-language support

---

## ✅ Project Status (प्रोजेक्ट स्थिति)

✅ **Completed Features:**
- Complete website with all pages
- Admin panel with full CRUD
- Service management system
- Inquiry system with service linking
- Responsive design for all devices
- Contact information integration
- Status badges (Active/Expired/Upcoming)
- Category filtering

✅ **Working:**
- All public pages
- Admin authentication
- Product management
- Service management
- Inquiry management
- Image uploads
- Responsive layout

---

**Last Updated:** February 2026
**Version:** 1.0.0
**Status:** Production Ready ✅
