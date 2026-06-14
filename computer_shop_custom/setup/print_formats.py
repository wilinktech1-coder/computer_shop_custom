import frappe


SALES_INVOICE_PRINT_FORMAT_NAME = "Computer Shop Bilingual Invoice"
PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME = "Computer Shop Professional Invoice"

SALES_INVOICE_HTML = """
{% set company_logo = frappe.db.get_value("Company", doc.company, "company_logo") if doc.company else None %}
{% set company_phone = frappe.db.get_value("Company", doc.company, "phone_no") if doc.company else None %}
{% set company_tax_id = frappe.db.get_value("Company", doc.company, "tax_id") if doc.company else None %}

<style>
    .cs-invoice {
        font-family: Arial, Tahoma, sans-serif;
        color: #1a1a1a;
        font-size: 12px;
        line-height: 1.45;
    }

    .cs-wrapper {
        border: 1px solid #c2cbd1;
        padding: 28px;
        background: #fff;
    }

    .cs-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 3px solid #1e3a8a;
        padding-bottom: 16px;
        margin-bottom: 22px;
    }

    .cs-logo-section {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .cs-logo {
        width: 72px;
        height: 72px;
        object-fit: contain;
    }

    .cs-logo-fallback {
        width: 72px;
        height: 72px;
        border: 2px solid #1e3a8a;
        color: #1e3a8a;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: 700;
    }

    .cs-company h1 {
        margin: 0;
        font-size: 22px;
        color: #1e3a8a;
        font-weight: 700;
        text-transform: uppercase;
    }

    .cs-company p {
        margin: 2px 0 0;
        color: #555;
    }

    .cs-invoice-details {
        text-align: right;
    }

    .cs-invoice-details h2 {
        margin: 0 0 8px;
        font-size: 28px;
        color: #1e3a8a;
        letter-spacing: 1px;
    }

    .cs-invoice-details table {
        margin-left: auto;
        border-collapse: collapse;
    }

    .cs-invoice-details th,
    .cs-invoice-details td {
        padding: 3px 8px;
        text-align: right;
    }

    .cs-invoice-details th {
        color: #555;
        font-weight: 600;
    }

    .cs-invoice-details td {
        font-weight: 700;
    }

    .cs-boxes {
        display: flex;
        justify-content: space-between;
        gap: 18px;
        margin-bottom: 22px;
    }

    .cs-box {
        flex: 1;
        padding: 12px;
        background: #f8fafc;
        border-left: 4px solid #1e3a8a;
    }

    .cs-box.cs-ar {
        text-align: right;
        direction: rtl;
        border-left: none;
        border-right: 4px solid #1e3a8a;
    }

    .cs-box h3 {
        margin: 0 0 8px;
        font-size: 12px;
        color: #1e3a8a;
        text-transform: uppercase;
        border-bottom: 1px solid #dde1e6;
        padding-bottom: 4px;
    }

    .cs-box p {
        margin: 4px 0;
        font-weight: 500;
    }

    .cs-items {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 18px;
    }

    .cs-items th,
    .cs-items td {
        border: 1px solid #cbd5e1;
        padding: 8px;
    }

    .cs-items th {
        background: #1e3a8a;
        color: #fff;
        text-align: center;
        font-weight: 600;
    }

    .cs-items tr:nth-child(even) {
        background: #f8fafc;
    }

    .cs-desc {
        text-align: left;
    }

    .cs-center {
        text-align: center;
    }

    .cs-right {
        text-align: right;
        white-space: nowrap;
    }

    .cs-summary-wrap {
        display: flex;
        justify-content: flex-end;
    }

    .cs-summary {
        width: 360px;
        border-collapse: collapse;
        border: 2px solid #1e3a8a;
    }

    .cs-summary th,
    .cs-summary td {
        padding: 9px 10px;
        text-align: right;
    }

    .cs-summary th {
        background: #f1f5f9;
        text-align: left;
        color: #333;
    }

    .cs-summary .cs-total th,
    .cs-summary .cs-total td {
        background: #1e3a8a;
        color: #fff;
        font-size: 16px;
        font-weight: 700;
    }

    .cs-words {
        margin-top: 16px;
        padding: 10px 12px;
        background: #f8fafc;
        border-left: 4px solid #1e3a8a;
    }

    .cs-footer {
        margin-top: 28px;
        border-top: 2px solid #dde1e6;
        padding-top: 14px;
        color: #64748b;
        font-size: 11px;
    }

    .cs-footer b {
        color: #1e3a8a;
    }
</style>

<div class="cs-invoice">
    <div class="cs-wrapper">
        <div class="cs-header">
            <div class="cs-logo-section">
                {% if company_logo %}
                    <img class="cs-logo" src="{{ company_logo }}" alt="Company Logo">
                {% else %}
                    <div class="cs-logo-fallback">{{ (doc.company or "C")[:1] }}</div>
                {% endif %}
                <div class="cs-company">
                    <h1>{{ doc.company or "" }}</h1>
                    <p>HQ Branch{% if company_phone %} | Phone: {{ company_phone }}{% endif %}</p>
                    {% if company_tax_id %}
                        <p>Tax ID / الرقم الضريبي: {{ company_tax_id }}</p>
                    {% endif %}
                </div>
            </div>

            <div class="cs-invoice-details">
                <h2>INVOICE / فاتورة</h2>
                <table>
                    <tr>
                        <th>Invoice No:</th>
                        <td>{{ doc.name }}</td>
                    </tr>
                    <tr>
                        <th>Date:</th>
                        <td>{{ frappe.utils.formatdate(doc.posting_date) }}</td>
                    </tr>
                    <tr>
                        <th>Currency:</th>
                        <td>{{ doc.currency }}</td>
                    </tr>
                </table>
            </div>
        </div>

        <div class="cs-boxes">
            <div class="cs-box">
                <h3>Billed To / فاتورة إلى</h3>
                <p>{{ doc.customer_name or doc.customer }}</p>
                {% if doc.customer_address %}
                    <p>{{ doc.customer_address }}</p>
                {% endif %}
                {% if doc.contact_mobile or doc.contact_email %}
                    <p>{{ doc.contact_mobile or "" }}{% if doc.contact_mobile and doc.contact_email %} | {% endif %}{{ doc.contact_email or "" }}</p>
                {% endif %}
            </div>

            <div class="cs-box cs-ar">
                <h3>Purchase Information / معلومات الشراء</h3>
                <p>Payment / الدفع: {% if doc.is_pos %}Cash / نقدا{% else %}Credit / آجل{% endif %}</p>
                {% if doc.due_date %}
                    <p>Due Date / تاريخ الاستحقاق: {{ frappe.utils.formatdate(doc.due_date) }}</p>
                {% endif %}
                {% if doc.owner %}
                    <p>Sales Rep / البائع: {{ doc.owner }}</p>
                {% endif %}
            </div>
        </div>

        <table class="cs-items">
            <thead>
                <tr>
                    <th style="width: 5%;">No<br>م</th>
                    <th style="width: 43%;">Description / التفاصيل</th>
                    <th style="width: 14%;">Unit Price<br>سعر الوحدة</th>
                    <th style="width: 12%;">Qty<br>الكمية</th>
                    <th style="width: 14%;">Tax<br>الضريبة</th>
                    <th style="width: 12%;">Total<br>الإجمالي</th>
                </tr>
            </thead>
            <tbody>
                {% for row in doc.items %}
                    <tr>
                        <td class="cs-center">{{ loop.index }}</td>
                        <td class="cs-desc">
                            <b>{{ row.item_name or row.item_code }}</b>
                            {% if row.description and row.description != row.item_name %}
                                <br>{{ row.description }}
                            {% endif %}
                        </td>
                        <td class="cs-right">{{ frappe.utils.fmt_money(row.rate, currency=doc.currency) }}</td>
                        <td class="cs-center">{{ row.qty }}</td>
                        <td class="cs-right">{{ frappe.utils.fmt_money(row.item_tax_amount or 0, currency=doc.currency) }}</td>
                        <td class="cs-right">{{ frappe.utils.fmt_money(row.amount, currency=doc.currency) }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>

        <div class="cs-summary-wrap">
            <table class="cs-summary">
                <tr>
                    <th>Net Total<br><span dir="rtl">الصافي</span></th>
                    <td>{{ frappe.utils.fmt_money(doc.net_total, currency=doc.currency) }}</td>
                </tr>
                <tr>
                    <th>Taxes & Charges<br><span dir="rtl">الضرائب والرسوم</span></th>
                    <td>{{ frappe.utils.fmt_money(doc.total_taxes_and_charges, currency=doc.currency) }}</td>
                </tr>
                {% if doc.discount_amount %}
                    <tr>
                        <th>Discount<br><span dir="rtl">الخصم</span></th>
                        <td>{{ frappe.utils.fmt_money(doc.discount_amount, currency=doc.currency) }}</td>
                    </tr>
                {% endif %}
                <tr class="cs-total">
                    <th>Grand Total<br><span dir="rtl">الإجمالي النهائي</span></th>
                    <td>{{ frappe.utils.fmt_money(doc.grand_total, currency=doc.currency) }}</td>
                </tr>
            </table>
        </div>

        {% if doc.in_words %}
            <div class="cs-words">
                <b>Amount in Words / المبلغ كتابة:</b> {{ doc.in_words }}
            </div>
        {% endif %}

        <div class="cs-footer">
            <b>Terms & Conditions:</b>
            {% if doc.terms %}
                {{ doc.terms }}
            {% else %}
                Payment due upon receipt. Standard hardware warranty applies. Returns within 14 days are subject to company policy.
            {% endif %}
        </div>
    </div>
</div>
"""


def install_sales_invoice_print_format():
    """Create or update the bilingual Sales Invoice print format."""
    values = {
        "print_format_name": SALES_INVOICE_PRINT_FORMAT_NAME,
        "doc_type": "Sales Invoice",
        "module": "Computer Shop Custom",
        "standard": "No",
        "custom_format": 1,
        "disabled": 0,
        "print_format_type": "Jinja",
        "html": SALES_INVOICE_HTML,
    }

    if frappe.db.exists("Print Format", SALES_INVOICE_PRINT_FORMAT_NAME):
        print_format = frappe.get_doc("Print Format", SALES_INVOICE_PRINT_FORMAT_NAME)
        print_format.update(values)
        print_format.save(ignore_permissions=True)
        action = "updated"
    else:
        print_format = frappe.get_doc({
            "doctype": "Print Format",
            "__newname": SALES_INVOICE_PRINT_FORMAT_NAME,
            **values,
        })
        print_format.insert(ignore_permissions=True)
        action = "created"

    frappe.db.commit()
    frappe.clear_cache(doctype="Sales Invoice")
    print(f"{SALES_INVOICE_PRINT_FORMAT_NAME} {action}")


PROFESSIONAL_SALES_INVOICE_HTML = """
{% set company_logo = frappe.db.get_value("Company", doc.company, "company_logo") if doc.company else None %}
{% set company_phone = frappe.db.get_value("Company", doc.company, "phone_no") if doc.company else None %}
{% set company_email = frappe.db.get_value("Company", doc.company, "email") if doc.company else None %}
{% set company_website = frappe.db.get_value("Company", doc.company, "website") if doc.company else None %}
{% set company_tax_id = frappe.db.get_value("Company", doc.company, "tax_id") if doc.company else None %}
{% set total_qty = doc.items | sum(attribute="qty") %}

<style>
    .pro-invoice {
        --ink: #111827;
        --muted: #64748b;
        --line: #d7dee8;
        --soft: #f5f7fb;
        --brand: #123c69;
        --brand-2: #0f766e;
        font-family: Arial, Tahoma, sans-serif;
        color: var(--ink);
        font-size: 11.5px;
        line-height: 1.45;
    }

    .pro-page {
        border: 1px solid var(--line);
        background: #fff;
    }

    .pro-top {
        display: grid;
        grid-template-columns: 1.3fr 0.9fr;
        gap: 22px;
        padding: 24px 28px 18px;
        border-top: 7px solid var(--brand);
        border-bottom: 1px solid var(--line);
    }

    .pro-brand {
        display: grid;
        grid-template-columns: 74px 1fr;
        gap: 14px;
        align-items: center;
    }

    .pro-logo,
    .pro-logo-mark {
        width: 74px;
        height: 74px;
        object-fit: contain;
    }

    .pro-logo-mark {
        display: flex;
        align-items: center;
        justify-content: center;
        border: 2px solid var(--brand);
        color: var(--brand);
        font-size: 28px;
        font-weight: 700;
    }

    .pro-company-name {
        margin: 0 0 4px;
        color: var(--brand);
        font-size: 23px;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
    }

    .pro-company-meta {
        color: var(--muted);
        font-size: 10.5px;
    }

    .pro-title {
        text-align: right;
    }

    .pro-title h1 {
        margin: 0;
        color: var(--brand);
        font-size: 31px;
        font-weight: 800;
        letter-spacing: 0;
    }

    .pro-title .ar {
        margin-top: 2px;
        color: var(--brand-2);
        direction: rtl;
        font-size: 18px;
        font-weight: 700;
    }

    .pro-status {
        display: inline-block;
        margin-top: 10px;
        padding: 4px 9px;
        border: 1px solid var(--line);
        border-radius: 999px;
        color: var(--muted);
        font-size: 10px;
        text-transform: uppercase;
    }

    .pro-section {
        padding: 18px 28px;
    }

    .pro-info-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 12px;
    }

    .pro-panel {
        min-height: 104px;
        border: 1px solid var(--line);
        background: var(--soft);
        padding: 12px;
    }

    .pro-panel h3 {
        margin: 0 0 9px;
        color: var(--brand);
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
    }

    .pro-panel p {
        margin: 3px 0;
    }

    .pro-panel .muted {
        color: var(--muted);
        font-size: 10px;
    }

    .pro-ar {
        direction: rtl;
        text-align: right;
    }

    .pro-kv {
        width: 100%;
        border-collapse: collapse;
    }

    .pro-kv th,
    .pro-kv td {
        padding: 3px 0;
        vertical-align: top;
    }

    .pro-kv th {
        width: 42%;
        color: var(--muted);
        font-weight: 600;
        text-align: left;
    }

    .pro-kv td {
        text-align: right;
        font-weight: 700;
    }

    .pro-items {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }

    .pro-items th {
        padding: 9px 7px;
        background: var(--brand);
        color: #fff;
        border: 1px solid var(--brand);
        font-size: 10px;
        text-align: center;
        text-transform: uppercase;
    }

    .pro-items td {
        padding: 8px 7px;
        border: 1px solid var(--line);
        vertical-align: top;
    }

    .pro-items tbody tr:nth-child(even) td {
        background: #fbfcfe;
    }

    .pro-no {
        width: 36px;
        text-align: center;
    }

    .pro-desc {
        width: 43%;
    }

    .pro-desc b {
        color: var(--ink);
        font-size: 11.5px;
    }

    .pro-desc .code {
        color: var(--muted);
        font-size: 10px;
    }

    .pro-center {
        text-align: center;
    }

    .pro-money {
        text-align: right;
        white-space: nowrap;
    }

    .pro-bottom {
        display: grid;
        grid-template-columns: 1fr 360px;
        gap: 18px;
        align-items: start;
        padding: 0 28px 22px;
    }

    .pro-note {
        border-left: 4px solid var(--brand-2);
        background: var(--soft);
        padding: 12px;
        min-height: 86px;
    }

    .pro-note h3 {
        margin: 0 0 7px;
        color: var(--brand);
        font-size: 11px;
        text-transform: uppercase;
    }

    .pro-note p {
        margin: 4px 0;
        color: var(--muted);
    }

    .pro-summary {
        width: 100%;
        border-collapse: collapse;
        border: 1px solid var(--line);
    }

    .pro-summary th,
    .pro-summary td {
        padding: 8px 10px;
        border-bottom: 1px solid var(--line);
    }

    .pro-summary th {
        background: var(--soft);
        color: var(--muted);
        text-align: left;
        font-weight: 700;
    }

    .pro-summary td {
        text-align: right;
        font-weight: 700;
        white-space: nowrap;
    }

    .pro-summary .grand th,
    .pro-summary .grand td {
        background: var(--brand);
        color: #fff;
        font-size: 15px;
        border-bottom: 0;
    }

    .pro-words {
        margin-top: 12px;
        padding: 10px 12px;
        border: 1px solid var(--line);
        color: var(--muted);
    }

    .pro-signatures {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 28px;
        padding: 8px 28px 24px;
    }

    .pro-sign {
        padding-top: 34px;
        border-top: 1px solid var(--line);
        color: var(--muted);
        text-align: center;
        font-size: 10px;
    }

    .pro-footer {
        padding: 11px 28px;
        background: var(--soft);
        border-top: 1px solid var(--line);
        color: var(--muted);
        font-size: 10px;
        text-align: center;
    }
</style>

<div class="pro-invoice">
    <div class="pro-page">
        <div class="pro-top">
            <div class="pro-brand">
                {% if company_logo %}
                    <img class="pro-logo" src="{{ company_logo }}" alt="Company Logo">
                {% else %}
                    <div class="pro-logo-mark">{{ (doc.company or "C")[:1] }}</div>
                {% endif %}
                <div>
                    <h2 class="pro-company-name">{{ doc.company or "" }}</h2>
                    <div class="pro-company-meta">
                        {% if doc.company_address_display %}
                            {{ doc.company_address_display }}
                        {% else %}
                            HQ Branch
                        {% endif %}
                        {% if company_phone %}<br>Phone: {{ company_phone }}{% endif %}
                        {% if company_email %} | Email: {{ company_email }}{% endif %}
                        {% if company_website %} | Web: {{ company_website }}{% endif %}
                        {% if company_tax_id %}<br>Tax ID / الرقم الضريبي: {{ company_tax_id }}{% endif %}
                    </div>
                </div>
            </div>

            <div class="pro-title">
                <h1>INVOICE</h1>
                <div class="ar">فاتورة مبيعات</div>
                <div class="pro-status">{{ doc.status or "Draft" }}</div>
            </div>
        </div>

        <div class="pro-section">
            <div class="pro-info-grid">
                <div class="pro-panel">
                    <h3>Bill To / العميل</h3>
                    <p><b>{{ doc.customer_name or doc.customer }}</b></p>
                    {% if doc.address_display %}
                        <p class="muted">{{ doc.address_display }}</p>
                    {% endif %}
                    {% if doc.contact_mobile or doc.contact_email %}
                        <p class="muted">{{ doc.contact_mobile or "" }}{% if doc.contact_mobile and doc.contact_email %} | {% endif %}{{ doc.contact_email or "" }}</p>
                    {% endif %}
                </div>

                <div class="pro-panel">
                    <h3>Invoice Details</h3>
                    <table class="pro-kv">
                        <tr><th>No.</th><td>{{ doc.name }}</td></tr>
                        <tr><th>Date</th><td>{{ frappe.utils.formatdate(doc.posting_date) }}</td></tr>
                        <tr><th>Due</th><td>{{ frappe.utils.formatdate(doc.due_date) if doc.due_date else "-" }}</td></tr>
                        <tr><th>Currency</th><td>{{ doc.currency }}</td></tr>
                    </table>
                </div>

                <div class="pro-panel pro-ar">
                    <h3>معلومات الفاتورة</h3>
                    <p>طريقة الدفع: {% if doc.is_pos %}نقدا{% else %}آجل{% endif %}</p>
                    <p>عدد الأصناف: {{ doc.items | length }}</p>
                    <p>إجمالي الكمية: {{ total_qty }}</p>
                    {% if doc.po_no %}
                        <p>طلب شراء: {{ doc.po_no }}</p>
                    {% endif %}
                </div>
            </div>
        </div>

        <div class="pro-section" style="padding-top: 0;">
            <table class="pro-items">
                <thead>
                    <tr>
                        <th class="pro-no">#<br>م</th>
                        <th class="pro-desc">Description / التفاصيل</th>
                        <th>Qty<br>الكمية</th>
                        <th>Unit Price<br>السعر</th>
                        <th>Discount<br>الخصم</th>
                        <th>Amount<br>الإجمالي</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in doc.items %}
                        <tr>
                            <td class="pro-no">{{ loop.index }}</td>
                            <td class="pro-desc">
                                <b>{{ row.item_name or row.item_code }}</b>
                                <div class="code">{{ row.item_code }}</div>
                                {% if row.description and row.description != row.item_name %}
                                    <div>{{ row.description }}</div>
                                {% endif %}
                            </td>
                            <td class="pro-center">{{ row.qty }} {{ row.uom or "" }}</td>
                            <td class="pro-money">{{ frappe.utils.fmt_money(row.rate, currency=doc.currency) }}</td>
                            <td class="pro-money">{{ frappe.utils.fmt_money(row.discount_amount or 0, currency=doc.currency) }}</td>
                            <td class="pro-money">{{ frappe.utils.fmt_money(row.amount, currency=doc.currency) }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>

        <div class="pro-bottom">
            <div>
                <div class="pro-note">
                    <h3>Terms & Notes / الشروط والملاحظات</h3>
                    {% if doc.terms %}
                        {{ doc.terms }}
                    {% else %}
                        <p>Payment is due according to the agreed terms.</p>
                        <p>Standard warranty applies according to manufacturer and company policy.</p>
                        <p class="pro-ar">تطبق شروط الضمان حسب سياسة الشركة والشركة المصنعة.</p>
                    {% endif %}
                </div>

                {% if doc.in_words %}
                    <div class="pro-words">
                        <b>Amount in Words / المبلغ كتابة:</b> {{ doc.in_words }}
                    </div>
                {% endif %}
            </div>

            <table class="pro-summary">
                <tr>
                    <th>Net Total / الصافي</th>
                    <td>{{ frappe.utils.fmt_money(doc.net_total, currency=doc.currency) }}</td>
                </tr>
                <tr>
                    <th>Taxes / الضريبة</th>
                    <td>{{ frappe.utils.fmt_money(doc.total_taxes_and_charges, currency=doc.currency) }}</td>
                </tr>
                {% if doc.discount_amount %}
                    <tr>
                        <th>Additional Discount / خصم إضافي</th>
                        <td>{{ frappe.utils.fmt_money(doc.discount_amount, currency=doc.currency) }}</td>
                    </tr>
                {% endif %}
                <tr class="grand">
                    <th>Grand Total / الإجمالي</th>
                    <td>{{ frappe.utils.fmt_money(doc.grand_total, currency=doc.currency) }}</td>
                </tr>
            </table>
        </div>

        <div class="pro-signatures">
            <div class="pro-sign">Prepared By / أعدت بواسطة</div>
            <div class="pro-sign">Customer Signature & Stamp / توقيع وختم العميل</div>
        </div>

        <div class="pro-footer">
            Thank you for your business | شكرا لتعاملكم معنا
        </div>
    </div>
</div>
"""


def install_professional_sales_invoice_print_format():
    """Create or update the professional Sales Invoice print format."""
    values = {
        "print_format_name": PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME,
        "doc_type": "Sales Invoice",
        "module": "Computer Shop Custom",
        "standard": "No",
        "custom_format": 1,
        "disabled": 0,
        "print_format_type": "Jinja",
        "html": PROFESSIONAL_SALES_INVOICE_HTML,
    }

    if frappe.db.exists("Print Format", PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME):
        print_format = frappe.get_doc("Print Format", PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME)
        print_format.update(values)
        print_format.save(ignore_permissions=True)
        action = "updated"
    else:
        print_format = frappe.get_doc({
            "doctype": "Print Format",
            "__newname": PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME,
            **values,
        })
        print_format.insert(ignore_permissions=True)
        action = "created"

    frappe.db.commit()
    frappe.clear_cache(doctype="Sales Invoice")
    print(f"{PROFESSIONAL_SALES_INVOICE_PRINT_FORMAT_NAME} {action}")
