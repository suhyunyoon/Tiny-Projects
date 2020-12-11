# first-react-app
This is my first full stack React web application.
It uses Node.js, Express, Webpack, React, ESLint, Nodemon and React.

This Project contains basic React components, Phonebook which can add and delete user.

## Quick Start

    # Clone repository
    git clone https://github.com/suhyunyoon/first-react-app
    
    cd first-react-app
    
    # Install npm dependencies
    npm install
    
    # Start dev server
    npm run dev
    
    # Build for production
    npm run build
    
    # Start production server
    npm start

## Documentation
### File Structure
All source files are in `src` directory. 
client `index.js` is located `src` directory
`src/resources` directory contains resource files, such as image and icon files.
`index.js` which runs server is in `src/server` directory.
`components` directory contains react components, which are  FirstApp and PhoneBook.

### Dependencies
This project uses Node.js, Express, Webpack, React, ESLint, Nodemon and React.
`.babelrc`, `.eslintrc.json`, `webpack.config.js`, `nodemon.json`are these config files.
Also this project can connect with MySQL server, its config file is `/config/db_config.json`.

### React function transfer
```mermaid
graph TB
A(App) -- onCreate=handleCreate --> B(PhoneForm.onCreate)
A -- onRemove=handleRemove --> C(PhoneInfoList.onRemove)
C --> D(PhoneInfo.onRemove)
