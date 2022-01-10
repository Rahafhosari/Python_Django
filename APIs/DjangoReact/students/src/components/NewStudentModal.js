import React, { useState, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewStudentForm from "./NewStudentForm";
import axios from "axios";

const NewStudentModal = (props) => {

    const [modal, setModal] = useState(false)
    // const [student, setStudent] = useState(initialState)

    // const createPerson = student => {
    //     axios.post('http://localhost:8000/api/student', student)
    //     .then(res=>{
    //         // setPeople([...people, res.data]);
    //     })
    // }
    // const toggle = () => {
    //     setModal(previous => ({
    //         modal: !previous.modal
    //     }));
    // };

    // var title = "Editing Student";
    // var button = <Button onClick={toggle}>Edit</Button>;
    // if (create) {
    //     title = "Creating New Student";
    //     button = (
    //         <Button
    //             color="primary"
    //             className="float-right"
    //             onClick={toggle}
    //             style={{ minWidth: "200px" }}
    //         >
    //             Create New
    //         </Button>
    //     );
    // }

    return (
    <Fragment>
        {/* {button}
        <Modal isOpen={modal} toggle={toggle}>
        <ModalHeader toggle={toggle}>{title}</ModalHeader>

        <ModalBody> */}
            <NewStudentForm
                initialName=""
                initialEmail=""
                initialDocument=""
                initialPhone=""
                onSubmitProp={createPerson}
            />
        {/* </ModalBody>
        </Modal> */}
    </Fragment>
    );

}

export default NewStudentModal;