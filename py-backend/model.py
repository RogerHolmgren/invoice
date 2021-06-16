import json

def commit(data, table):
    with open(table, 'w') as f:
        json.dump(data, f)

def saveCustomer(data, customer):
    data['customers'].append(customer)
    commit(data, 'customers.json')

def saveInvoice(data, invoice):
    data['invoice'].append(invoice)
    commit(data, 'invoices.json')

def getCustomers():
    with open('customers.json') as f:
        data = json.load(f)
    return data

def getInvoice(num):
    with open('invoices.json') as f:
        data = json.load(f)

    for invoice in data['invoices']:
        if num == invoice['invoice_nr']:
            return invoice
