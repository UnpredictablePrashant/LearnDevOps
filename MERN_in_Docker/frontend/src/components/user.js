import React from 'react';

class Userdetail extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            items: [],
            dataIsLoaded: false
        };
    }
    // {
    //     mode:'cors',
    //     headers:{
    //         'Access-COntrol-Allow-Origin': '*'
    //     }
    // }
    componentDidMount(){
        fetch("http://localhost:3001/fetchAllEntry")
        .then(res => res.json())
        .then(json => {
            this.setState({
                items: json,
                dataIsLoaded: true
            })
        })
    }
    render(){
        const {dataIsLoaded, items} =  this.state;
        if(!dataIsLoaded) {
            return (<div>
                <h1>Please wait...</h1>
            </div>)
        }
       
        return(
            <div>
                <h1>Hello World!</h1>
                {items.map(item => (
                    <div>
                        <h1>{item.name}</h1>
                        <h1>{item.age}</h1>
                    </div>
                ))}
            </div>
        );         
    }
}

export default Userdetail;