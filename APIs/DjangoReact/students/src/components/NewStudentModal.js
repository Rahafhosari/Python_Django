import React, { useState, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewStudentForm from "./NewStudentForm";

const NewStudentModal = (props) => {

    const [modal, setModal] = useState(false)
    const {create, student} = props

    const toggle = () => {
        setModal(previous => ({
            modal: !previous.modal
        }));
    };

    var title = "Editing Student";
    var button = <Button onClick={toggle}>Edit</Button>;
    if (create) {
        title = "Creating New Student";

        button = (
            <Button
                color="primary"
                className="float-right"
                onClick={toggle}
                style={{ minWidth: "200px" }}
            >
                Create New
            </Button>
        );
    }

    return (
    <Fragment>
        {button}
        <Modal isOpen={modal} toggle={toggle}>
        <ModalHeader toggle={toggle}>{title}</ModalHeader>

        <ModalBody>
            <NewStudentForm
                // resetState={resetState}
                toggle={toggle}
                student={student}
            />
        </ModalBody>
        </Modal>
    </Fragment>
    );

}

export default NewStudentModal;