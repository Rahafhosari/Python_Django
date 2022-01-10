import React from "react";
import { Table, UncontrolledCollapse, Button, CardBody, Card } from 'reactstrap';
import NewStudentModal from "./NewStudentModal";
import ConfirmRemovalModal from "./ConfirmRemovalModal";

const StudentList = (props) => {
    const {students} = props

    //New created student carried by props
    
    return (
      <>
      <Table dark>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Document</th>
            <th>Phone</th>
            <th>Registration</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!students || students.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            students.map(student => (
              <tr key={student.pk}>
                <td>{student.name}</td>
                <td>{student.email}</td>
                <td>{student.document}</td>
                <td>{student.phone}</td>
                <td>{student.registrationDate}</td>
                <td align="center">
                  {/* <NewStudentModal
                    create={false}
                    student={student}
                    // resetState={this.props.resetState}
                  /> */}
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={student.pk}
                    // resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
    
      <div>
        <Button color="primary" id="toggler" style={{ marginBottom: '1rem' }}>
          Add New Student
        </Button>
        <UncontrolledCollapse toggler="#toggler">
          <Card>
            <CardBody>
              <NewStudentModal
                create={false}
                // student={student}
                // resetState={this.props.resetState}
              />
            </CardBody>
          </Card>
        </UncontrolledCollapse>
      </div>
        </Table>
      </>
    );
}

export default StudentList;