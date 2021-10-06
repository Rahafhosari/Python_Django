import React, {useState} from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

const NewStudentForm = (props) => {

    const [pk, setPk] = useState(0)
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [document, setDocument] = useState("")
    const [phone, setPhone] = useState("")

    const {student, resetState, toggle} = props
// const onSubmitHandler = e => {
//     e.preventDefault();
//     axios.post("http://localhost:8000/api/author", {
//         name: name,
//     })
//         .then(() => navigate("/"))
//         .catch(err => {
//             const errorResponse = err.response.data.errors;
//             const errorArray = [];
//             for (const key of Object.keys(errorResponse)) { // Loop through all errors and get the messages
//                 errorArray.push(errorResponse[key].message)
//             }
//             // Set Errors
//             setErrors(errorArray);
//         })
// }

const createStudent = e => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/students', 
        pk,
        name,
        email,
        document,
        phone
    )
    .then(() => {
        resetState();
        toggle();
    });
};

const editStudent = e => {
    e.preventDefault();
    axios.put('http://localhost:8000/api/students' + pk, 
        name,
        email,
        document,
        phone
    )
    .then(() => {
        resetState();
        toggle();
    });
};

// const defaultIfEmpty = (value) => {
//     return value === "" ? "" : value;
// };


return (
        <Form onSubmit={student ? editStudent : createStudent}>
        <FormGroup>
            <Label for="name">Name:</Label>
            <Input
            type="text"
            name="name"
            onChange={(e)=>setName(e.target.value)}
            // value = {student.name}
            // value={defaultIfEmpty(student.name)}
            />
        </FormGroup>
        <FormGroup>
            <Label for="email">Email:</Label>
            <Input
            type="email"
            name="email"
            onChange={(e)=>setEmail(e.target.value)}
            value = {student.email}
            // value={defaultIfEmpty(email)}
            />
        </FormGroup>
        <FormGroup>
            <Label for="document">Document:</Label>
            <Input
            type="text"
            name="document"
            onChange={(e)=>setDocument(e.target.value)}
            value = {student.document}
            // value={defaultIfEmpty(document)}
            />
        </FormGroup>
        <FormGroup>
            <Label for="phone">Phone:</Label>
            <Input
            type="text"
            name="phone"
            onChange={(e)=>setPhone(e.target.value)}
            value = {student.phone}
            // value={defaultIfEmpty(phone)}
            />
        </FormGroup>
        <Button>Send</Button>
        </Form>
    );

}

export default NewStudentForm;