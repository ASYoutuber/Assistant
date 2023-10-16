from tkinter import *
from tkinter import ttk
from currency_converter import CurrencyConverter

list_ = []
codes = []

def Currency_list():
    Currencies = (	("AFN", "Afghani"),
        ("DZD", "Algerian Dinar"),
        ("ARS", "Argentine Peso"),
        ("AMD", "Armenian Dram"),
        ("AWG", "Aruban Guilder"),
        ("AUD", "Australian Dollar"),
        ("AZN", "Azerbaijanian Manat"),
        ("BSD", "Bahamian Dollar"),
        ("BHD", "Bahraini Dinar"),
        ("THB", "Baht"),
        ("PAB", "Balboa"),
        ("BBD", "Barbados Dollar"),
        ("BYR", "Belarussian Ruble"),
        ("BZD", "Belize Dollar"),
        ("BMD", "Bermudian Dollar"),
        ("VEF", "Bolivar Fuerte"),
        ("BOB", "Boliviano"),
        ("BRL", "Brazilian Real"),
        ("BND", "Brunei Dollar"),
        ("BGN", "Bulgarian Lev"),
        ("BIF", "Burundi Franc"),
        ("CAD", "Canadian Dollar"),
        ("CVE", "Cape Verde Escudo"),
        ("KYD", "Cayman Islands Dollar"),
        ("GHS", "Cedi"),
        ("CLP", "Chilean Peso"),
        ("COP", "Colombian Peso"),
        ("KMF", "Comoro Franc"),
        ("CDF", "Congolese Franc"),
        ("BAM", "Convertible Mark"),
        ("NIO", "Cordoba Oro"),
        ("CRC", "Costa Rican Colon"),
        ("HRK", "Croatian Kuna"),
        ("CUP", "Cuban Peso"),
        ("CZK", "Czech Koruna"),
        ("GMD", "Dalasi"),
        ("DKK", "Danish Krone"),
        ("MKD", "Denar"),
        ("DJF", "Djibouti Franc"),
        ("STD", "Dobra"),
        ("DOP", "Dominican Peso"),
        ("VND", "Dong"),
        ("XCD", "East Caribbean Dollar"),
        ("EGP", "Egyptian Pound"),
        ("SVC", "El Salvador Colon"),
        ("ETB", "Ethiopian Birr"),
        ("EUR", "Euro"),
        ("FKP", "Falkland Islands Pound"),
        ("FJD", "Fiji Dollar"),
        ("HUF", "Forint"),
        ("GIP", "Gibraltar Pound"),
        ("XAU", "Gold"),
        ("HTG", "Gourde"),
        ("PYG", "Guarani"),
        ("GNF", "Guinea Franc"),
        ("GYD", "Guyana Dollar"),
        ("HKD", "Hong Kong Dollar"),
        ("UAH", "Hryvnia"),
        ("ISK", "Iceland Krona"),
        ("INR", "Indian Rupee"),
        ("IRR", "Iranian Rial"),
        ("IQD", "Iraqi Dinar"),
        ("JMD", "Jamaican Dollar"),
        ("JOD", "Jordanian Dinar"),
        ("KES", "Kenyan Shilling"),
        ("PGK", "Kina"),
        ("LAK", "Kip"),
        ("KWD", "Kuwaiti Dinar"),
        ("MWK", "Kwacha"),
        ("AOA", "Kwanza"),
        ("MMK", "Kyat"),
        ("GEL", "Lari"),
        ("LVL", "Latvian Lats"),
        ("LBP", "Lebanese Pound"),
        ("ALL", "Lek"),
        ("HNL", "Lempira"),
        ("SLL", "Leone"),
        ("RON", "Leu"),
        ("LRD", "Liberian Dollar"),
        ("LYD", "Libyan Dinar"),
        ("SZL", "Lilangeni"),
        ("LTL", "Lithuanian Litas"),
        ("LSL", "Loti"),
        ("MGA", "Malagasy Ariary"),
        ("MYR", "Malaysian Ringgit"),
        ("MUR", "Mauritius Rupee"),
        ("MZN", "Metical"),
        ("MXN", "Mexican Peso"),
        ("MDL", "Moldovan Leu"),
        ("MAD", "Moroccan Dirham"),
        ("BOV", "Mvdol"),
        ("NGN", "Naira"),
        ("ERN", "Nakfa"),
        ("NAD", "Namibia Dollar"),
        ("NPR", "Nepalese Rupee"),
        ("ANG", "Netherlands Antillean Guilder"),
        ("ILS", "New Israeli Sheqel"),
        ("TMT", "New Manat"),
        ("TWD", "New Taiwan Dollar"),
        ("NZD", "New Zealand Dollar"),
        ("KPW", "North Korean Won"),
        ("NOK", "Norwegian Krone"),
        ("MRO", "Ouguiya"),
        ("PKR", "Pakistan Rupee"),
        ("XPD", "Palladium"),
        ("MOP", "Pataca"),
        ("TOP", "Pa’anga"),
        ("CUC", "Peso Convertible"),
        ("UYU", "Peso Uruguayo"),
        ("PHP", "Philippine Peso"),
        ("XPT", "Platinum"),
        ("GBP", "Pound Sterling"),
        ("BWP", "Pula"),
        ("QAR", "Qatari Rial"),
        ("GTQ", "Quetzal"),
        ("ZAR", "Rand"),
        ("BTN", "Ngultrum"),
        ("OMR", "Rial Omani"),
        ("KHR", "Riel"),
        ("PEN", "Nuevo Sol"),
        ("MVR", "Rufiyaa"),
        ("IDR", "Rupiah"),
        ("RUB", "Russian Ruble"),
        ("RWF", "Rwanda Franc"),
        ("SHP", "Saint Helena Pound"),
        ("SAR", "Saudi Riyal"),
        ("RSD", "Serbian Dinar"),
        ("SCR", "Seychelles Rupee"),
        ("XAG", "Silver"),
        ("SGD", "Singapore Dollar"),
        ("SBD", "Solomon Islands Dollar"),
        ("KGS", "Som"),
        ("SOS", "Somali Shilling"),
        ("TJS", "Somoni"),
        ("ZAR", "South African Rand"),
        ("LKR", "Sri Lanka Rupee"),
        ("XSU", "Sucre"),
        ("SDG", "Sudanese Pound"),
        ("SRD", "Surinam Dollar"),
        ("SEK", "Swedish Krona"),
        ("CHF", "Swiss Franc"),
        ("SYP", "Syrian Pound"),
        ("BDT", "Taka"),
        ("WST", "Tala"),
        ("TZS", "Tanzanian Shilling"),
        ("KZT", "Tenge"),
        ("TTD", "Trinidad and Tobago Dollar"),
        ("MNT", "Tugrik"),
        ("TND", "Tunisian Dinar"),
        ("TRY", "Turkish Lira"),
        ("AED", "UAE Dirham"),
        ("USD", "US Dollar"),
        ("UGX", "Uganda Shilling"),
        ("COU", "Unidad de Valor Real"),
        ("CLF", "Unidades de fomento"),
        ("UYI", "Uruguay Peso en Unidades Indexadas (URUIURUI)"),
        ("UZS", "Uzbekistan Sum"),
        ("VUV", "Vatu"),
        ("KRW", "Won"),
        ("YER", "Yemeni Rial"),
        ("JPY", "Yen"),
        ("CNY", "Yuan Renminbi"),
        ("ZMK", "Zambian Kwacha"),
        ("ZWL", "Zimbabwe Dollar"),
        ("PLN", "Zloty"),
    )
    for i in Currencies:
        list_.append(i[1])
        codes.append(i[0])

Currency_list()

def Currency_Convert_app():
    window = Tk()

    title = Label(window, text = "Welcome to Currency Converter!", bg = "cyan", fg = "white", font = ("Times New Roman", 40), width = 45)
    com_1 = ttk.Combobox(window, values = list_, font = ("Times New Roman", 20), width = 25)
    txt = Entry(window, width = 25)
    com_2 = ttk.Combobox(window, values = list_, font = ("Times New Roman", 20), width = 25)
    result = Label(window)
    btn = Button(window, text = "Submit", font = ("Times New Roman", 20), width = 25, command = lambda: Convert(txt, com_1, com_2, result))

    title.grid(row = 0, column = 2)
    com_1.grid(row = 1, column = 2)
    com_2.grid(row = 2, column = 2)
    txt.grid(row = 3, column = 2)
    btn.grid(row = 4, column = 2)
    result.grid(row = 5, column = 2)

    window.geometry("900x600")
    window.title("Currency Converter")
    window.mainloop()

def Convert(txt, com_1, com_2, result):
    get1 = int(txt.get())
    com1 = str(com_1.get())
    symbol1 = list_.index(com1)
    code1 = codes[symbol1]
    com2 = str(com_2.get())
    symbol2 = list_.index(com2)
    code2 = codes[symbol2]
    c = CurrencyConverter()
    try:
        result.configure(text = str(round(c.convert(get1, code1, code2), 2)), bg = "cyan", fg = "white", font = ("Times New Roman", 20), width = 25)
    except:
        result.configure(text = "This currency is not supported!", bg = "cyan", fg = "white", font = ("Times New Roman", 20), width = 25)