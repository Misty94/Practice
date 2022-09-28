import React from 'react';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
// import ButtonGroup from '@material-ui/core/ButtonGroup';
import Container from '@material-ui/core/Container';
// import AcUnitOutlinedIcon from '@mui/icons-material/AcUnitOutlined';
// import SendIcon from '@mui/icons-material/Send';
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import { makeStyles } from '@material-ui/core';

const useStyles = makeStyles({
    btn: {
        fontSize: 60,
        backgroundColor: 'violet',
        '&:hover': {
            backgroundColor: 'blue'
        }
    }, 
    title: {
        textDecoration: 'underline',
        marginBottom: 20
    }
})

const Create = () => {
    const classes = useStyles();

    return (
        <div>
            <Container>
                <Typography
                    className={classes.title}
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
                    className={classes.btn}
                    onClick={ () => console.log("You clicked me!")}
                    type='submit'
                    color='secondary'
                    variant='contained'
                    // startIcon={<SendIcon />}
                    endIcon={<KeyboardArrowRightIcon />}
                    // disableElevation
                    // variant='outlined'
                >
                    Submit
                </Button>
                {/* <br />
                <AcUnitOutlinedIcon />
                <AcUnitOutlinedIcon color='secondary' fontSize='large'/>
                <AcUnitOutlinedIcon color='secondary' fontSize='small'/>
                <AcUnitOutlinedIcon color='action' fontSize='small'/>
                <AcUnitOutlinedIcon color='error' fontSize='small'/>
                <AcUnitOutlinedIcon color='disabled' fontSize='small'/> */}
                {/* <ButtonGroup
                    color='secondary'
                    variant='contained'
                >
                    <Button>One</Button>
                    <Button>Two</Button>
                    <Button>Three</Button>
                </ButtonGroup> */}
            </Container>
        </div>
    )
}

export default Create;