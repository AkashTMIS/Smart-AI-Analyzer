# Enable editing mode
        if st.button("Update Role Info"):
            st.session_state.editing = True
            # Store original values in case of cancel
            st.session_state.original_description = role_info["description"]
            st.session_state.original_required_skills = role_info["required_skills"][:]
            st.session_state.original_technical_skills = role_info["recommended_skills"]["technical"][:]
            st.session_state.original_soft_skills = role_info["recommended_skills"]["soft"][:]

        # Editing Mode
        if st.session_state.editing:
            new_description = st.text_area("Update Job Description", role_info["description"])
            new_required_skills = st.text_area("Update Required Skills (comma-separated)", ", ".join(role_info["required_skills"]))
            new_technical_skills = st.text_area("Update Recommended Technical Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["technical"]))
            new_soft_skills = st.text_area("Update Recommended Soft Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["soft"]))

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Save"):
                    role_info["description"] = new_description
                    role_info["required_skills"] = [skill.strip() for skill in new_required_skills.split(",")]
                    role_info["recommended_skills"]["technical"] = [skill.strip() for skill in new_technical_skills.split(",")]
                    role_info["recommended_skills"]["soft"] = [skill.strip() for skill in new_soft_skills.split(",")]
                    st.session_state.editing = False
                    st.success("Job role information updated!")

                    # Write to JSON file
                    with open("job_roles.json", "w") as file:
                        json.dump(st.session_state.job_roles, file, indent=4)

            with col2:
                if st.button("Cancel"):
                    # Revert changes
                    role_info["description"] = st.session_state.original_description
                    role_info["required_skills"] = st.session_state.original_required_skills
                    role_info["recommended_skills"]["technical"] = st.session_state.original_technical_skills
                    role_info["recommended_skills"]["soft"] = st.session_state.original_soft_skills
                    st.session_state.editing = False