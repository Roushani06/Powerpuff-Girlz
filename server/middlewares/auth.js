import jwt from 'jsonwebtoken';
import 'dotenv/config';

const userAuth = async (req, res, next) => {
    const {token} = req.headers;
    if(!token){
        return res.status(401).json({message: "Access denied"});
    }

    try{
        const tokenDecode = jwt.verify(token, process.env.JWT_SECRET);
        

        if(tokenDecode.id){
           req.body.userId = tokenDecode.id;
        }else{
            return res.json({success: false, message: "Not Authorized"});
        }

        next();
    }
    catch(error){
        console.log(error);
        res.json({success: false, message: `An error occurred: ${error.message}`});
    }
        
       
};

export default userAuth;
