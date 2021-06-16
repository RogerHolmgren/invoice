import { Link } from "react-router-dom";

const Customers = () => {
    return (
        <div>
            <h2>Kundregister</h2>
            <li>Roger</li>
            <li>Josefin</li>
            <Link to='/'>Tillbaka</Link>
        </div>
    )
}

export default Customers
