import express from "express";
import { createLawyer, getAllLawyers } from "../controllers/lawyerController.js";

const lawyerRouter = express.Router();

lawyerRouter.post("/", createLawyer);      // POST /api/lawyers
lawyerRouter.get("/", getAllLawyers);      // GET /api/lawyers

export default lawyerRouter;