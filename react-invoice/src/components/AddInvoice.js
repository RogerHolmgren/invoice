import { useState } from "react";

const AddInvoice = ({ onAdd }) => {
  const [invoiceNr, setInvoiceNr] = useState("");
  const [customerNr, setCustomerNr] = useState("");
  const [customer, setCustomer] = useState("");
  const [day, setDay] = useState("");
  const [checkbox, setCheckbox] = useState(false);

  const onSubmit = (e) => {
    e.preventDefault();

    onAdd({ invoiceNr, customerNr, customer, day, checkbox });
  };

  return (
    <form className="add-form" onSubmit={onSubmit}>
      <div className="form-control">
        <label>Faktura nr</label>
        <input
          type="text"
          value={invoiceNr}
          onChange={(e) => setInvoiceNr(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label>Kund nr</label>
        <input
          type="text"
          value={customerNr}
          onChange={(e) => setCustomerNr(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label>Faktura Datum</label>
        <input
          type="text"
          placeholder="ÅÅ/MM/DD"
          value={day}
          onChange={(e) => setDay(e.target.value)}
        />
      </div>
      <div className="form-control">
        <label>Kund</label>
        <input
          type="text"
          value={customer}
          onChange={(e) => setCustomer(e.target.value)}
        />
      </div>
      <div className="form-control form-control-check">
        <label>checkbox</label>
        <input
          type="checkbox"
          checked={checkbox}
          value={checkbox}
          onChange={(e) => setCheckbox(e.currentTarget.checked)}
        />
      </div>

      <input type="submit" value="Skapa faktura" className="btn btn-block" />
    </form>
  );
};

export default AddInvoice;
