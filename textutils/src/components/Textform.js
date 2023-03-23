import React,{useState} from 'react'

export default function Textform(props) {
    const [text, setText] = useState("Enter text");
    const handleUpClick =()=>{
        let newText=text.toUpperCase();
        setText(newText);
    }
    const handleLowClick =()=>{
        let newText=text.toLowerCase();
        setText(newText);
    }
    const handleOnClick =()=>{
      if(text==="Enter text")
      setText('');
    }
    const handleOnChange =(event)=>{
        setText(event.target.value);
    }
    
    const handleReverse =()=> {
      let splitText=text.split('');
      let revText=splitText.reverse();
      let newText=splitText.join('');
      setText(newText);
    }
    const speak =()=> {
      let msg=new SpeechSynthesisUtterance();
      msg.text=text;
      window.speechSynthesis.speak(msg);
        }
      
    
  return (
 <>
 <div className="container" style={{color:props.mode==='dark'?'white':'black'}}>
    <h3>{props.heading}</h3>
    <div className="mb-3 my-3">
  <textarea className="form-control" id="myBox" onClick={handleOnClick} onChange={handleOnChange} style={{backgroundColor: props.mode==='dark'?'#7EC8E3':'white',color:props.mode==='dark'?'#050A30':'black'}} value={text} rows="8"></textarea>
</div>
<button className="btn btn-success" onClick={handleUpClick}>Convert to upper case</button>
<button className="btn btn-success mx-3" onClick={handleLowClick}>Convert to lower case</button>
<button className="btn btn-success" onClick={handleReverse}>Reverse</button>

<div className="container my-3">
 <h3>Preview: </h3> 
  <p>{text.length>0?text:"Please enter text first!!!"}</p>
<p>Entered text contains {text.length} letters</p>
<p>Entered text contains {text.length > 0? text.split(" ").length : 0} words</p>
</div>
<div className="container">
<button type="submit" className="btn btn-success mx-2 my-2" onClick={speak}>Dictate</button>
</div>
</div></>
  )
}
