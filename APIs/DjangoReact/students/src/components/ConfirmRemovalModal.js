import React, { useState, Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

const ConfirmRemovalModal = () => {

  const [modal, setModal] = useState(false)

  const toggle = () => {
    setModal(previous => ({
      modal: !previous.modal
    }));
  };

  const deleteStudent = pk => {
    axios.delete(API_URL + pk).then(() => {
      // this.props.resetState();
      toggle();
    });
  };

    return (
      <Fragment>
        <Button color="danger" onClick={() => toggle()}>
          Remove
        </Button>
        <Modal isOpen={modal} toggle={toggle}>
          <ModalHeader toggle={toggle}>
            Do you really wanna delete the student?
          </ModalHeader>

          <ModalFooter>
            <Button type="button" onClick={() => toggle()}>
              Cancel
            </Button>
            <Button
              type="button"
              color="primary"
              onClick={() => deleteStudent(this.props.pk)}
            >
              Yes
            </Button>
          </ModalFooter>
        </Modal>
      </Fragment>
    );
}

export default ConfirmRemovalModal;