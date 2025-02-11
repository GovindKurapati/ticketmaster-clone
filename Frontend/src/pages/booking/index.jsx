import {
  Box,
  Flex,
  Heading,
  Text,
  Input,
  Button,
  Stack,
} from "@chakra-ui/react";
import { useState } from "react";

function BookingPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    cardNumber: "",
    expirationDate: "",
    cvv: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here (e.g., API call)
    console.log("Form submitted:", formData);
  };

  return (
    <Box maxW="800px" mx="auto" p={8}>
      <Heading as="h1" fontSize="3xl" mb={6} textAlign={"center"}>
        Complete Your Booking
      </Heading>
      {/* Event Information */}
      <Box mb={8} p={6} bg="gray.50" borderRadius="md" boxShadow="sm">
        <Heading as="h1" fontSize="2xl" mb={4}>
          Amazing Concert 2024
        </Heading>
        <Text fontSize="md" color="gray.600" mb={4}>
          Join us for an unforgettable night of music with some of the best
          artists in the industry! This concert will feature live performances
          from top artists across various genres, creating a night full of
          energy and excitement.
        </Text>
        <Text fontSize="md" color="gray.700">
          <strong>Venue:</strong> Madison Square Garden, New York City, NY
        </Text>
        <Text fontSize="md" color="gray.700">
          <strong>Date & Time:</strong> Saturday, December 14, 2024 - 7:00 PM
        </Text>
      </Box>

      {/* Form */}
      <Box
        as="form"
        onSubmit={handleSubmit}
        bg="gray.50"
        borderRadius="md"
        boxShadow="sm"
        mb={8}
        p={6}
      >
        <Stack spacing={6}>
          {/* User Information */}
          <Box>
            <Heading as="h2" fontSize="2xl" mb={4}>
              User Information
            </Heading>
            <Input
              placeholder="Full Name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              mb={4}
            />
            <Input
              placeholder="Email"
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              mb={4}
            />
            <Input
              placeholder="Phone Number"
              name="phone"
              type="tel"
              value={formData.phone}
              onChange={handleChange}
              mb={4}
            />
          </Box>

          {/* Payment Information */}
          <Box>
            <Heading as="h2" fontSize="2xl" mb={4}>
              Payment Information
            </Heading>
            <Input
              placeholder="Card Number"
              name="cardNumber"
              value={formData.cardNumber}
              onChange={handleChange}
              mb={4}
            />
            <Flex gap={4}>
              <Input
                placeholder="Expiration Date (MM/YY)"
                name="expirationDate"
                value={formData.expirationDate}
                onChange={handleChange}
                mb={4}
              />
              <Input
                placeholder="CVV"
                name="cvv"
                type="password"
                value={formData.cvv}
                onChange={handleChange}
                mb={4}
                maxW="100px"
              />
            </Flex>
          </Box>

          {/* Submit Button */}
          <Button
            colorScheme="blue"
            size="lg"
            w={{ base: "100%", md: "auto" }}
            px={12}
            py={6}
            type="submit"
          >
            Confirm Booking
          </Button>
        </Stack>
      </Box>
    </Box>
  );
}

export default BookingPage;
