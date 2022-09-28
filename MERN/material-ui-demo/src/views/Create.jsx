import React from 'react';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Container from '@material-ui/core/Container';

const Create = () => {
    return (
        <div>
            <Container>
                <Typography
                    variant='h6'
                    component='h2'
                    gutterBottom
                    color='textSecondary'
                    // noWrap
                    // align='center'
                >
                    Create a New Note
                </Typography>
                <Button
                    onClick={ () => console.log("You clicked me!")}
                    type='submit'
                    color='secondary'
                    variant='contained'
                    // disableElevation
                    // variant='outlined'
                >
                    Submit
                </Button>
                <ButtonGroup
                    color='secondary'
                    variant='contained'
                >
                    <Button>One</Button>
                    <Button>Two</Button>
                    <Button>Three</Button>
                </ButtonGroup>
            </Container>
        </div>
    )
}

export default Create;