import {
  Box,
  Flex,
  Heading,
  Text,
  Input,
  Button,
  Checkbox,
  Link,
  Select,
} from "@chakra-ui/react";
import { useState } from "react";
import useAuthStore from "../../store/useAuthStore";
import { useNavigate } from "react-router-dom";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function SignUp() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    Email: "",
    PasswordHash: "",
    FirstName: "",
    LastName: "",
    CountryOfResidence: "",
    ZipCode: "",
    DateOfBirth: "",
    PhoneNumber: "",
  });

  const { signup, loading } = useAuthStore();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Submit", formData);
    try {
      await signup(formData);
      // Redirect or take further action after successful signup
      // Show success notification
      toast.success("Signup successful!");

      // Clear form data or redirect user after successful signup
      setFormData({
        Email: "",
        PasswordHash: "",
        FirstName: "",
        LastName: "",
        CountryOfResidence: "",
        ZipCode: "",
        DateOfBirth: "",
        PhoneNumber: "",
      });
      navigate("/");
    } catch (error) {
      toast.error("Error during signup. Please try again.");
    }
  };

  return (
    <Flex
      minH="100vh"
      align="center"
      justify="center"
      bg="gray.50"
      width={"100%"}
    >
      <ToastContainer />
      <Box
        maxW="1200px"
        w="full"
        bg="white"
        boxShadow="lg"
        borderRadius="md"
        overflow="hidden"
        display={{ base: "block", md: "flex" }}
      >
        {/* Left Section */}
        <Box
          w={{ base: "100%", md: "40%" }}
          bgImage="url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6RQlc6supPZNxQTfOXhbp0Th-Y_2HLt7C1w&s')"
          bgSize="cover"
          p={8}
          color="white"
          textAlign="left"
          display="flex"
          flexDirection="column"
          bgColor="#121212"
          position={"relative"}
          _before={{
            content: '""',
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            bgGradient:
              "linear(to-r, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 100%)",
            zIndex: 1, // Overlay above the background image but below content
          }}
        >
          <Flex zIndex={"2"} flexDirection={"column"}>
            <Heading
              fontSize={{ base: "3xl", md: "4xl" }}
              mb={4}
              color="#00ffff"
            >
              Your All-Access Pass
            </Heading>
            <Text
              fontSize={{ base: "md", md: "lg" }}
              mb={6}
              color={"brand.secondary"}
            >
              This is it — millions of live events, up-to-the-minute alerts for
              your favorite artists and teams and, of course, always safe,
              secure ticketing.
            </Text>
          </Flex>
        </Box>

        {/* Right Section (Sign Up Form) */}
        <Box w={{ base: "100%", md: "60%" }} p={8}>
          <Heading fontSize="2xl" mb={4}>
            Sign Up
          </Heading>
          <Text mb={4}>
            Create a new Ticketmaster account. Already have an account?{" "}
            <Link color="brand.primary" href="/login">
              Sign In
            </Link>
          </Text>

          {/* Form */}
          <Box as="form" onSubmit={handleSubmit}>
            {/* Email */}
            <Input
              name="Email"
              placeholder="Email"
              value={formData.Email}
              mb={4}
              onChange={handleChange}
            />

            {/* Password */}
            <Input
              placeholder="Password"
              name="PasswordHash"
              type="password"
              value={formData.PasswordHash}
              mb={4}
              onChange={handleChange}
            />

            {/* First Name / Last Name */}
            <Flex gap={4} mb={4}>
              <Input
                name="FirstName"
                value={formData.FirstName}
                placeholder="First Name"
                onChange={handleChange}
              />
              <Input
                name="LastName"
                placeholder="Last Name"
                value={formData.LastName}
                onChange={handleChange}
              />
            </Flex>

            <Flex gap={4} mb={4}>
              <Input
                placeholder="Date of Birth (MM/DD/YYYY)"
                name="DateOfBirth"
                type="date" // Date input type for better UX
                value={formData.DateOfBirth}
                onChange={handleChange}
              />
              <Input
                placeholder="Phone Number"
                name="PhoneNumber"
                type="tel" // Tel input type for phone number validation
                value={formData.PhoneNumber}
                onChange={handleChange}
              />
            </Flex>

            {/* Country of Residence / Zip Code */}
            <Flex gap={4} mb={4}>
              <Select
                placeholder="Country of Residence"
                onChange={handleChange}
                name="CountryOfResidence"
                value={formData.CountryOfResidence}
              >
                <option value="US">United States</option>
                {/* Add more countries as needed */}
              </Select>
              <Input
                name="ZipCode"
                value={formData.ZipCode}
                placeholder="Zip/Postal Code"
                onChange={handleChange}
              />
            </Flex>

            {/* Agree to Terms */}
            <Checkbox mb={6}>
              I agree to the <Link color="brand.primary">Terms of Use</Link> and{" "}
              <Link color="brand.primary">Privacy Policy</Link>.
            </Checkbox>

            {/* Sign Up Button */}
            <Button
              colorScheme="blue"
              w="full"
              isLoading={loading}
              type="submit"
            >
              Sign Up
            </Button>

            {/* Terms of Use and Privacy Policy */}
            <Text mt={4} fontSize="sm" color="gray.500">
              By continuing past this page, you agree to the{" "}
              <Link color="brand.primary">Terms of Use</Link> and understand
              that your information will be used as described in our{" "}
              <Link color="brand.primary">Privacy Policy</Link>.
            </Text>
          </Box>
        </Box>
      </Box>
    </Flex>
  );
}

export default SignUp;
