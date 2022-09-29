import React, { useState } from 'react';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
// import ButtonGroup from '@material-ui/core/ButtonGroup';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormLabel from '@material-ui/core/FormLabel';
import FormControl from '@material-ui/core/FormControl';
// import AcUnitOutlinedIcon from '@mui/icons-material/AcUnitOutlined';
// import SendIcon from '@mui/icons-material/Send';
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import { FormControlLabel, makeStyles } from '@material-ui/core';

const useStyles = makeStyles({
    field: {
        marginTop: 20,
        marginBottom: 20,
        display: 'block'
    }
    // btn: {
    //     fontSize: 60,
    //     backgroundColor: 'violet',
    //     '&:hover': {
    //         backgroundColor: 'blue'
    //     }
    // }, 
    // title: {
    //     textDecoration: 'underline',
    //     marginBottom: 20
    // }
})

const Create = () => {
    const classes = useStyles();
    const [title, setTitle] = useState("");
    const [details, setDetails] = useState("");
    const [titleError, setTitleError] = useState(false);
    const [detailsError, setDetailsError] = useState(false);
    const [category, setCategory] = useState('todos')

    const handleSubmit = (e) => {
        e.preventDefault()
        setTitleError(false);
        setDetailsError(false);
        if (title === ''){
            setTitleError(true)
        }
        if (details === ''){
            setDetailsError(true)
        }
        if (title && details){
            console.log(title, details, category)
        }
    }

    return (
        <div>
            <Container>
                <Typography
                    // className={classes.title}
                    variant='h6'
                    component='h2'
                    gutterBottom
                    color='textSecondary'
                    // noWrap
                    // align='center'
                >
                    Create a New Note
                </Typography>
                <form noValidate autoComplete='off' onSubmit={handleSubmit}>
                    <TextField 
                        onChange={(e) => setTitle(e.target.value)}
                        className={classes.field}
                        label="Note Title"
                        variant='outlined'
                        color='secondary'
                        fullWidth
                        required
                        error={titleError}
                    />
                    <TextField 
                        onChange={(e) => setDetails(e.target.value)}
                        className={classes.field}
                        label="Details"
                        variant='outlined'
                        color='secondary'
                        multiline
                        minRows={4}
                        fullWidth
                        required
                        error={detailsError}
                    />
                    <FormControl className={classes.field}>
                        <FormLabel>Note Category</FormLabel>
                        <RadioGroup value={category} onChange={(e) => setCategory(e.target.value)}>
                            <FormControlLabel value='money' control={<Radio />} label="Money" />
                            <FormControlLabel value='todos' control={<Radio />} label="Todos" />
                            <FormControlLabel value='reminders' control={<Radio />} label="Reminders" />
                            <FormControlLabel value='work' control={<Radio />} label="Work" />
                            {/* has to have value prop */}
                            {/* <Radio value='hello'/>
                            <Radio value='goodbye'/> */}
                        </RadioGroup>
                    </FormControl>
                    <Button
                    // className={classes.btn}
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
                </form>
                
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