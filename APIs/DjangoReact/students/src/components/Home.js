import React, { useState, useEffect } from "react";
import { Col, Container, Row } from "reactstrap";
import StudentList from "./StudentList";
import NewStudentModal from "./NewStudentModal";

import axios from "axios";


const Home = () => {

  const [students, setStudents] = useState([])

  
  useEffect( () => {
    axios.get('http://localhost:8000/api/students')
        .then(response => setStudents((response.data)))
        .catch(error => console.log("There was an issue: ", error))
},[])

    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <StudentList
              students={students}
              // resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            {/* <NewStudentModal 
              create={true} 
              // resetState={this.resetState} 
            /> */}
          </Col>
        </Row>
      </Container>
    );
}

export default Home;