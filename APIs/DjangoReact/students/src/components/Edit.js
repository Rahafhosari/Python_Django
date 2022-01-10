import React, { useState, useEffect } from "react";
import NewStudentForm from "./NewStudentForm";


const Edit = (props) => {
    // const initialState = {
    //     username: "",
    //     email: "",
    //     password: "",
    //     passwordConfirmation: ""
    // };
    const { initialFirstName, initialLastName, onSubmitProp } = props;

    return (
        <div>
            <NewStudentForm />
        </div>
    )
}

export default Edit
