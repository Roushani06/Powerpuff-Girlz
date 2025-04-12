import Lawyer from "../models/LawyerSchema.js";
import bcrypt from "bcrypt";

// CREATE lawyer


export const createLawyer = async (req, res) => {
  try {
    const {
      name,
      email,
      phone,
      password,
      specialization,
      experience,
      location,
      bio,
      available,
      profilePic,
      certificates,
    } = req.body;

    // Hash the password securely
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    const lawyer = new Lawyer({
      name,
      email,
      phone,
      password: hashedPassword,
      specialization,
      experience,
      location,
      bio,
      available,
      profilePic,
      certificates,
    });

    await lawyer.save();
    res.status(201).json({ message: "Lawyer created successfully", lawyer });
  } catch (error) {
    console.error("Error creating lawyer:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
};






// GET all lawyers (with optional query filters)
export const getAllLawyers = async (req, res) => {
  try {
    const filters = req.query; // example: ?specialization=Civil&location=Delhi
    const lawyers = await Lawyer.find(filters);
    res.status(200).json(lawyers);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
