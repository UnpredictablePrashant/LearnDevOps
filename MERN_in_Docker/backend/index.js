const express = require('express')
const mongoose = require('mongoose')
const bodyparser = require('body-parser')
var cors = require('cors')


const app = express()

app.use(cors());


mongoose.connect('mongodb://mongo:27017/dockermongoreact')

const user = {
    name: {
        type: String
    },
    age: {
        type: Number
    }
}

const User = mongoose.model('userDetail',user)

app.use(bodyparser.json())

app.get('/hello',(req,res)=>{
    res.send('Hello World!')
})

app.post('/addEntry',(req,res)=>{
    console.log(req.body)
    const user1 = new User({
        name: req.body.name, 
        age: req.body.age
    })
    user1.save((err,result)=>{
        if(err){
            res.send("Something went wrong!")
        }else{
            res.send('Data added')
        }
    })
})

app.get('/fetchAllEntry',(req,res)=>{
    User.find({},(err,docs)=>{
        if(err){
            res.send("Something went wrong!")
        }else{
            res.send(docs)
        }
    })
})

app.listen(3001, ()=>{
    console.log("Server started at port 3001")
})
