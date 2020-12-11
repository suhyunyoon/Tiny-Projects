// file: src/components/PhoneBook/PhoneForm.js
import React, { Component } from 'react';

class PhoneForm extends Component{
	// Initialize
	state = {
		name: '',
		phone: ''
	}
	// When name or phoneNum are changed
	handleChange = (e) => {
		this.setState({
			[e.target.name]: e.target.value
		})
	}
		
	// When Submit button pressed
	handleSubmit = (e) => {
		// Prevent page reloading
		e.preventDefault();
		// Transfer data to parent components
		this.props.onCreate(this.state);
		// Initialize(For new PhoneBook)
		this.setState({
			name: '',
			phone: ''
		})
	}

	// render
	render(){
		return (
			<form onSubmit={this.handleSubmit}>
				<input
					placeholder="이름"
					value={this.state.name}
					onChange={this.handleChange}
					name="name"
				/>
				<input
					placeholder="전화번호"
					value={this.state.phone}
					onChange={this.handleChange}
					name="phone"
				/>
				<button type="submit">등록</button>
				<br />
			</form>
		);
	}
}

export default PhoneForm;
