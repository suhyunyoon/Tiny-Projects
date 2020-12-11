import React, { Component } from 'react';
import PhoneForm from './PhoneForm';
import PhoneInfoList from './PhoneInfoList';

class App extends Component {
	id = 2;
	state = {
		info: [
			{
				id: 0,
				name: '김민준',
				phone: '010-0000-0000'
			},
			{
				id: 1,
				name: '홍길동',
				phone: '010-1234-4576'
			}
		],
		keyword: '',
		users: []
	};
	// find Input was changed
	handleChange = (e) => {
		this.setState({
			keyword: e.target.value,
		});
	}
	// When Input new Phonebook
	handleCreate = (data) => {
		const { info } = this.state;
		this.setState({
			info: info.concat({ id: this.id++, ...data })
		})
		console.log(data);
	}
	// When Remove Phonebook(Button pressed)
	handleRemove = (id) => {
		const { info } = this.state;
		//console.log("Remove called");
		this.setState({
			info: info.filter(member => member.id !== id)
		})
	}
	// When data Updated
	handleUpdate = (id, data) => {
		const { info } = this.state;
		this.setState({
			info: info.map(
				member => id === member.id
				? { ...member, ...data}
				: member
			)
		});
	}
	
	componentDidMount() {
		fetch('/api/getUsername')
    		.then(res => res.json())
			.then(user => {
				//console.log(user);
				return this.setState({ users: user.username })});
  	}

	// render
	render() {
		const { info, keyword } = this.state;
		const filteredList = info.filter(
			member => member.name.indexOf(keyword) !== -1
		);
		return (
			<div>
				<p> Hello {this.state.users}! </p>
				<PhoneForm 
					onCreate={this.handleCreate}
				/>
				<input 
					placeholder="검색 할 이름을 입력하세요"
					onChange={this.handleChange}
					value={keyword}
				/>
				<hr />
				<PhoneInfoList 
					data={filteredList}
					onRemove={this.handleRemove}
					onUpdate={this.handleUpdate}
				/>
			</div>
		);
	}
}

export default App;
