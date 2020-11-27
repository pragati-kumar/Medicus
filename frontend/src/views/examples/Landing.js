/*!

=========================================================

*/
import React, { useEffect, useRef } from "react";
// nodejs library that concatenates classes
import classnames from "classnames";

// reactstrap components
import {
  Badge,
  Button,
  Card,
  CardBody,
  CardImg,
  FormGroup,
  Input,
  InputGroupAddon,
  InputGroupText,
  InputGroup,
  Container,
  Row,
  Col,
} from "reactstrap";

// core components
import DemoNavbar from "components/Navbars/DemoNavbar.js";
import CardsFooter from "components/Footers/CardsFooter.js";

// index page sections
import Download from "../IndexSections/Download.js";

const Landing = (props) => {
  const main = useRef(0);
  const hiddenFileInput = useRef(null);
  const handleClick = (event) => {
    hiddenFileInput.current.click();
  };
  const handleChange = (event) => {
    const fileUploaded = event.target.files[0];
    //handle file upload here
  };

  useEffect(() => {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
  }, []);

  return (
    <>
      <DemoNavbar />
      <main ref={main}>
        <div className="position-relative">
          {/* shape Hero */}
          <section className="section section-lg section-shaped pb-250">
            <div className="shape shape-style-1 shape-default">
              <span />
              <span />
              <span />
              <span />
              <span />
              <span />
              <span />
              <span />
              <span />
            </div>
            <Container className="py-lg-md d-flex">
              <div className="col px-0">
                <Row>
                  <Col lg="6">
                    <h1 className="display-3 text-white">
                      Your very own diagnostic tool{" "}
                    </h1>
                    <p className="lead text-white">
                      Just upload a picture of a Chest X-ray to get a diagnosis
                      from our highly accurate Deep Learning Model
                    </p>
                    <div className="btn-wrapper">
                      <Button
                        className="btn-icon mb-3 mb-sm-0"
                        color="info"
                        href="#"
                      >
                        <span className="btn-inner--icon mr-1">
                          <i className="ni ni-sound-wave" />
                        </span>
                        <span className="btn-inner--text">Get Analysis</span>
                      </Button>
                      <Button
                        className="btn-white btn-icon mb-3 mb-sm-0 ml-1"
                        color="default"
                        onClick={handleClick}
                        type="file"
                      >
                        <span className="btn-inner--icon mr-1">
                          <i className="ni ni-cloud-upload-96" />
                        </span>
                        <span className="btn-inner--text">Upload an X-ray</span>
                      </Button>
                      <input
                        type="file"
                        ref={hiddenFileInput}
                        onChange={handleChange}
                        style={{ display: "none" }}
                      />
                    </div>
                  </Col>
                  <Col lg="6">
                    <Card className="card-lift--hover shadow border-0">
                      <CardBody className="py-5">
                        <div className="icon icon-shape icon-shape-primary rounded-circle mb-4">
                          <i className="ni ni-check-bold" />
                        </div>
                        <h6 className="text-primary text-uppercase">
                          Your X-ray Report
                        </h6>
                        <p className="description mt-3">
                          Argon is a great free UI package based on Bootstrap 4
                          that includes the most important components and
                          features.
                        </p>
                        <div>
                          <Badge color="danger" pill className="mr-1">
                            Viral
                          </Badge>
                          <Badge color="danger" pill className="mr-1">
                            Bacterial
                          </Badge>
                          <Badge color="success" pill className="mr-1">
                            Normal
                          </Badge>
                        </div>
                        <Button
                          className="mt-4"
                          color="primary"
                          href="#pablo"
                          onClick={(e) => e.preventDefault()}
                        >
                          Learn more
                        </Button>
                      </CardBody>
                    </Card>
                  </Col>
                </Row>
              </div>
            </Container>
            {/* SVG separator */}
            <div className="separator separator-bottom separator-skew">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                preserveAspectRatio="none"
                version="1.1"
                viewBox="0 0 2560 100"
                x="0"
                y="0"
              >
                <polygon
                  className="fill-white"
                  points="2560 0 2560 100 0 100"
                />
              </svg>
            </div>
          </section>
          {/* 1st Hero Variation */}
        </div>
      </main>
    </>
  );
};

export default Landing;
